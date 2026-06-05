import re
from datetime import datetime, timedelta

SIGNAL_WORDS = {
    "indonesia_nickel": {
        "critical": [
            "RKAB", "配额.*削减", "配额.*收紧", "配额.*调整", "配额.*减少",
            "印尼.*停产", "印尼.*检修", "印尼.*暂停",
            "华飞.*投产", "华飞.*达产", "华飞.*试产", "华飞.*开工", "Pomalaa",
            "镍.*特许权", "印尼.*出口禁",
            "镍价.*大涨", "镍价.*大跌", "镍价.*暴", "镍价.*创新",
            "印尼.*镍矿.*赶走", "印尼.*镍.*冲突", "印尼.*镍.*禁",
        ],
        "important": [
            "印尼.*镍", "镍.*配额", "镍矿.*政策", "能矿部",
            "华越", "华科", "湿法冶炼", "高冰镍",
            "华友.*印尼", "印尼.*华友",
            "红土镍矿", "镍价", "镍.*产能", "镍.*产量",
            "印尼.*政策", "印尼.*矿业", "印尼.*矿.*新政",
            "镍.*减产", "镍.*过剩", "镍.*供需", "镍.*库存",
            "印尼.*难", "印尼.*受限", "印尼.*紧缩",
        ],
        "context": [
            "印尼", "镍", "不锈钢", "新能源.*镍", "三元.*镍",
        ],
    },
    "lithium": {
        "critical": [
            "津巴布韦.*批文", "出口批文", "出口禁令", "暂停.*锂.*出口",
            "硫酸锂.*投产", "硫酸锂.*达产", "硫酸锂.*试产",
            "碳酸锂.*大涨", "碳酸锂.*大跌", "碳酸锂.*暴", "碳酸锂.*创",
            "锂价.*大涨", "锂价.*大跌", "锂价.*暴", "锂价.*突破",
            "华友.*锂.*签约", "华友.*锂.*合同",
            "Arcadia", "华景科技",
        ],
        "important": [
            "华友.*锂", "碳酸锂价格", "氢氧化锂", "硫酸锂",
            "津巴布韦.*锂", "锂矿出口", "锂精矿",
            "碳酸锂", "锂价", "锂矿", "锂盐",
            "锂.*产能", "锂.*库存", "锂.*供需",
        ],
        "context": [
            "锂", "新能源.*锂", "电池.*锂", "锂电",
        ],
    },
    "cashflow": {
        "critical": [
            "华友.*定增", "华友.*增发", "华友.*可转债", "华友.*融资",
            "华友.*业绩预告", "华友.*季报", "华友.*年报",
            "华友.*现金流.*大幅", "华友.*资产负债率.*上升",
            "华友.*评级.*下调", "华友.*信用",
            "华友.*增资", "华友.*募集",
            "华友.*净利润.*增", "华友.*净利润.*降",
            "华友.*业绩.*增", "华友.*业绩.*降", "华友.*业绩.*翻",
        ],
        "important": [
            "华友.*现金流", "华友.*资本开支",
            "华友.*资产负债", "华友.*负债率",
            "华友.*在建工程", "华友.*投资",
            "华友.*营收", "华友.*利润", "华友.*业绩",
            "华友.*分红", "华友.*派息",
            "华友.*股价", "华友.*涨", "华友.*跌",
            "华友.*年报.*点评", "华友.*研报",
            "华友.*市值", "华友.*估值",
        ],
        "context": [
            "华友钴业", "华友", "603799",
        ],
    },
    "europe_cathode": {
        "critical": [
            "匈牙利.*投产", "匈牙利.*量产", "匈牙利.*出货",
            "华友.*LGES", "华友.*LG新能源", "华友.*亿纬",
            "华友.*正极.*签约", "华友.*正极.*合同", "华友.*正极.*长单",
            "欧洲.*正极.*关税", "CBAM.*正极", "IRA.*正极",
        ],
        "important": [
            "匈牙利.*正极", "匈牙利.*产线", "华友.*匈牙利",
            "欧洲.*正极材料", "欧洲.*本土化",
            "正极材料.*加工费", "正极材料.*价格",
            "三元正极", "高镍正极", "超高镍",
            "LGES", "亿纬锂能.*华友",
        ],
        "context": [
            "正极材料", "正极", "cathode", "前驱体",
        ],
    },
    "cobalt_copper": {
        "critical": [
            "钴价.*大涨", "钴价.*大跌", "钴价.*暴", "钴价.*创",
            "铜价.*大涨", "铜价.*大跌", "铜价.*暴", "铜价.*创",
            "铜价.*新高", "铜价.*突破",
            "刚果金.*禁令", "刚果金.*停产", "刚果金.*冲突",
            "刚果金.*战略储备", "刚果金.*出口.*禁", "刚果金.*储备",
            "固态电池.*量产", "固态电池.*突破",
        ],
        "important": [
            "钴价", "钴.*供给", "钴.*需求", "钴.*库存",
            "铜价.*走强", "铜价.*走势", "铜价.*同步", "铜价",
            "刚果金.*钴", "DRC.*cobalt",
            "华友.*钴", "华友.*铜",
            "钴.*产量", "钴.*产能",
            "钴.*报价", "钴.*稳定", "钴.*坚挺",
            "铜.*创.*高", "铜.*四年",
        ],
        "context": [
            "钴", "铜", "cobalt", "copper",
        ],
    },
}

RECENCY_BOOST = {
    1: 1.5,   # today
    3: 1.3,   # 2-3 days
    7: 1.2,   # this week
    14: 1.1,  # 2 weeks
    30: 1.0,  # this month
    60: 0.7,  # 2 months
}


def _match_score(text: str, patterns: list[str]) -> int:
    count = 0
    for pat in patterns:
        if re.search(pat, text):
            count += 1
    return count


def _recency_multiplier(date_str: str) -> float:
    if not date_str:
        return 0.7
    try:
        dt = datetime.strptime(date_str[:10], "%Y-%m-%d")
        days = (datetime.now() - dt).days
        for threshold, mult in sorted(RECENCY_BOOST.items()):
            if days <= threshold:
                return mult
        return 0.6
    except (ValueError, TypeError):
        return 0.7


def score_news_item(category_id: str, item: dict) -> dict:
    signals = SIGNAL_WORDS.get(category_id, {})
    text = f"{item.get('title', '')} {item.get('summary', '')}"

    crit = _match_score(text, signals.get("critical", []))
    imp = _match_score(text, signals.get("important", []))
    ctx = _match_score(text, signals.get("context", []))

    base = crit * 10 + imp * 3 + ctx * 1
    recency = _recency_multiplier(item.get("date", ""))
    score = base * recency

    within_month = recency >= 1.0
    within_week = recency >= 1.2

    if crit >= 2 and within_month:
        level = "critical"
        label = "关键"
    elif crit >= 1 and imp >= 1 and within_month:
        level = "critical"
        label = "关键"
    elif crit >= 1 and within_week:
        level = "critical"
        label = "关键"
    elif crit >= 1 and within_month:
        level = "important"
        label = "重要"
    elif imp >= 2 and within_month:
        level = "important"
        label = "重要"
    elif crit >= 1 or imp >= 2:
        level = "normal"
        label = "参考"
    elif imp >= 1:
        level = "normal"
        label = "参考"
    elif ctx >= 1:
        level = "low"
        label = "相关"
    else:
        level = "low"
        label = "相关"

    return {
        **item,
        "score": round(score, 1),
        "level": level,
        "label": label,
        "crit_hits": crit,
        "imp_hits": imp,
    }


def analyze_category(category_id: str, news_items: list[dict]) -> dict:
    scored = [score_news_item(category_id, item) for item in news_items]
    scored.sort(key=lambda x: x["score"], reverse=True)

    critical_items = [i for i in scored if i["level"] == "critical"]
    important_items = [i for i in scored if i["level"] == "important"]

    brief = _generate_brief(category_id, critical_items, important_items, scored)

    if len(critical_items) >= 2:
        status = "alert"
        status_label = "有关键变动"
    elif critical_items or len(important_items) >= 3:
        status = "watch"
        status_label = "有重要动态"
    else:
        status = "stable"
        status_label = "暂无重大变化"

    return {
        "brief": brief,
        "status": status,
        "status_label": status_label,
        "critical_count": len(critical_items),
        "important_count": len(important_items),
        "news": scored,
    }


def _generate_brief(
    category_id: str,
    critical: list[dict],
    important: list[dict],
    all_items: list[dict],
) -> str:
    parts = []

    if critical:
        signals = []
        for item in critical[:3]:
            title = item["title"]
            title = re.sub(r"\s*[-–—|]\s*(新浪财经|东方财富|搜狐网|观察者|财富号|证券时报|雪球|澎湃|腾讯|凤凰|每日经济|第一财经|同花顺|虎嗅|界面|财联社|36氪|新京报|前瞻网|中国金融信息网|上海有色.*|thepaper\.cn|cb\.com\.cn|Mitrade|财富号.*|东方财富网|搜狐.*|观察者网|Yicai Global).*$", "", title)
            title = re.sub(r"\s*-\s*\S+$", "", title)
            if len(title) > 40:
                title = title[:38] + "…"
            signals.append(title)
        parts.append(f"⚠️ {len(critical)} 条关键信号：" + "；".join(signals) + "。")

    if important:
        parts.append(f"另有 {len(important)} 条重要动态值得关注。")

    if not critical and not important:
        parts.append("近期暂无直接影响该变量的关键信息，建议持续跟踪。")

    recent_dates = [i.get("date", "")[:10] for i in all_items[:5] if i.get("date")]
    if recent_dates:
        latest = max(recent_dates)
        parts.append(f"信息截至 {latest}。")

    return " ".join(parts)
