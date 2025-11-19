from datetime import datetime


def normalize_article(raw):
    return {
        "title": raw.get("headline", ""),
        "content": raw.get("summary", ""),
        "source": raw.get("source", "unknown"),
        "url": raw.get("url", ""),
        "published_at": datetime.utcfromtimestamp(raw.get("datetime", 0)).isoformat(),
        "symbol": raw.get("related", ""),
    }
