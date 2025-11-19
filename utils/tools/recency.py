from datetime import datetime, timezone
import math

def add_recency_weight(articles):
    now = datetime.now(timezone.utc)

    for a in articles:
        published = datetime.fromisoformat(a["published_at"])

        # If result is naive → convert to UTC
        if published.tzinfo is None:
            published = published.replace(tzinfo=timezone.utc)

        days_old = (now - published).days
        a["age_days"] = days_old
        a["recency_weight"] = math.exp(-0.1 * days_old)

    return articles
