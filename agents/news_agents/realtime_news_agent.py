from utils.finnhub_client import finnhub_client
from utils.tools.normalize import normalize_article
from utils.tools.filter import filter_relevant_articles
from utils.tools.dedupe import dedupe_articles
from utils.tools.src_credibility import apply_credibility
from utils.tools.recency import add_recency_weight


def fetch_news_for_company(symbol: str, from_date: str, to_date: str):
    """Fetch news articles for a given company symbol within a date range.
    Args:
        symbol (str): Stock symbol of the company.
        from_date (str): Start date in YYYY-MM-DD format.
        to_date (str): End date in YYYY-MM-DD format.
    Returns:
        list: List of news articles.
    """
    try:
        raw_news = finnhub_client.company_news(symbol, _from=from_date, to=to_date)

        # Step 1: Filter relevance
        filtered = filter_relevant_articles(raw_news, symbol)

        # Step 2: Dedupe
        deduped = dedupe_articles(filtered)

        # Step 3: Normalize
        normalized = [normalize_article(a) for a in deduped]

        # Step 4: Credibility scoring
        with_cred = apply_credibility(normalized)

        # Step 5: Recency weighting
        final_news = add_recency_weight(with_cred)

        return final_news

    except Exception as e:
        print("Error fetching news:", e)
        return []



if __name__ == "__main__":
    apple_news = fetch_news_for_company('AAPL', '2025-11-18', '2025-11-18')
    print(len(apple_news), "news articles about Apple fetched.")
    print(apple_news[:2])