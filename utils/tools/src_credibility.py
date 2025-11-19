

SOURCE_WEIGHTS = {
    "reuters": 1.0,
    "bloomberg": 0.95,
    "wsj": 0.90,
    "cnbc": 0.80,
    "yahoo": 0.60,
    "reddit": 0.25
}

def apply_credibility(articles):
    for a in articles:
        src = a["source"].lower()
        a["credibility"] = SOURCE_WEIGHTS.get(src, 0.5)
    return articles
