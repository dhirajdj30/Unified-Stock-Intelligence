


def filter_relevant_articles(articles, symbol):
    filtered = []
    for art in articles:
        related = art.get("related", "")
        if symbol.upper() in related.upper():
            if len(art.get("summary", "")) > 20:  # avoid junk
                filtered.append(art)
    return filtered
