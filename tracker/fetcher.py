import re
import time
import logging
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

import feedparser
import requests
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}

_cache: dict[str, tuple[float, list]] = {}
CACHE_TTL = 300  # 5 minutes


def _clean_html(raw: str) -> str:
    return BeautifulSoup(raw, "html.parser").get_text(strip=True) if raw else ""


def search_google_news(keyword: str, limit: int = 8) -> list[dict]:
    q = urllib.parse.quote(keyword)
    url = f"https://news.google.com/rss/search?q={q}&hl=zh-CN&gl=CN&ceid=CN:zh-Hans"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
        resp.raise_for_status()
        feed = feedparser.parse(resp.text)
        results = []
        for entry in feed.entries[:limit]:
            pub_date = ""
            if hasattr(entry, "published_parsed") and entry.published_parsed:
                pub_date = time.strftime("%Y-%m-%d %H:%M", entry.published_parsed)
            source = ""
            if hasattr(entry, "source") and hasattr(entry.source, "title"):
                source = entry.source.title
            results.append({
                "title": _clean_html(entry.get("title", "")),
                "url": entry.get("link", ""),
                "date": pub_date,
                "source": source,
                "summary": _clean_html(entry.get("summary", ""))[:200],
            })
        return results
    except Exception as e:
        logger.warning("Google News fetch failed for %s: %s", keyword, e)
        return []


def search_baidu_news(keyword: str, limit: int = 8) -> list[dict]:
    q = urllib.parse.quote(keyword)
    url = f"https://www.baidu.com/s?wd={q}&tn=news&rtt=4&bsst=1"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        results = []
        for item in soup.select(".result")[:limit]:
            title_el = item.select_one("h3 a")
            if not title_el:
                continue
            source_el = item.select_one(".c-color-gray, .c-color-gray2, .news-source .c-gap-right")
            date_el = item.select_one(".c-color-gray2, .c-font-normal")
            results.append({
                "title": title_el.get_text(strip=True),
                "url": title_el.get("href", ""),
                "date": date_el.get_text(strip=True) if date_el else "",
                "source": source_el.get_text(strip=True) if source_el else "",
                "summary": "",
            })
        return results
    except Exception as e:
        logger.warning("Baidu News fetch failed for %s: %s", keyword, e)
        return []


def search_eastmoney(keyword: str, limit: int = 6) -> list[dict]:
    q = urllib.parse.quote(keyword)
    url = f"https://so.eastmoney.com/news/s?keyword={q}"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        results = []
        for item in soup.select(".news-item, .result-item, .search-item")[:limit]:
            title_el = item.select_one("a.title, h3 a, a")
            if not title_el:
                continue
            results.append({
                "title": title_el.get_text(strip=True),
                "url": title_el.get("href", ""),
                "date": "",
                "source": "东方财富",
                "summary": "",
            })
        return results
    except Exception as e:
        logger.warning("Eastmoney fetch failed for %s: %s", keyword, e)
        return []


def fetch_category_news(keywords: list[str], limit_per_keyword: int = 5) -> list[dict]:
    cache_key = "|".join(sorted(keywords))
    now = time.time()
    if cache_key in _cache:
        ts, data = _cache[cache_key]
        if now - ts < CACHE_TTL:
            return data

    all_results = []
    seen_titles = set()

    def _fetch_one(kw):
        items = search_google_news(kw, limit=limit_per_keyword)
        if len(items) < 2:
            items.extend(search_baidu_news(kw, limit=limit_per_keyword))
        return items

    with ThreadPoolExecutor(max_workers=5) as pool:
        futures = {pool.submit(_fetch_one, kw): kw for kw in keywords}
        for future in as_completed(futures):
            try:
                items = future.result()
                for item in items:
                    norm = re.sub(r"\s+", "", item["title"])
                    if norm and norm not in seen_titles:
                        seen_titles.add(norm)
                        all_results.append(item)
            except Exception:
                pass

    all_results.sort(key=lambda x: x.get("date", ""), reverse=True)
    all_results = all_results[:20]
    _cache[cache_key] = (now, all_results)
    return all_results
