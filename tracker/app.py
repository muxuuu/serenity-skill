import logging

from flask import Flask, jsonify, render_template

from analyzer import analyze_category
from config import CATEGORIES
from fetcher import fetch_category_news

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", categories=CATEGORIES)


@app.route("/api/news/<category_id>")
def api_news(category_id):
    cat = next((c for c in CATEGORIES if c["id"] == category_id), None)
    if not cat:
        return jsonify({"error": "unknown category"}), 404
    raw_news = fetch_category_news(cat["keywords"])
    result = analyze_category(cat["id"], raw_news)
    result["category"] = cat["name"]
    return jsonify(result)


@app.route("/api/categories")
def api_categories():
    return jsonify(CATEGORIES)


if __name__ == "__main__":
    app.run(debug=True, port=5999)
