from utils.finnhub_client import finnhub_client



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
        news = finnhub_client.company_news(symbol, _from=from_date, to=to_date)
        return news
    except Exception as e:
        print("Error fetching news:", e)
        return []






if __name__ == "__main__":
    apple_news = fetch_news_for_company('AAPL', '2025-11-18', '2025-11-18')
    print(len(apple_news), "news articles about Apple fetched.")
    print(apple_news)