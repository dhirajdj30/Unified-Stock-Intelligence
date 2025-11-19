



def dedupe_articles(articles):
    seen = set()
    unique = []
    for a in articles:
        key = a["headline"].lower()
        if key not in seen:
            unique.append(a)
            seen.add(key)
    return unique
