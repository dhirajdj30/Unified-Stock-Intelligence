import os
from dotenv import load_dotenv
import finnhub
load_dotenv()

api_key = os.getenv("FINNHUB_API")


finnhub_client = finnhub.Client(api_key=api_key)



if __name__ == "__main__":
    try:
        news = finnhub_client.company_news('AAPL', _from="2025-11-18", to="2025-11-18")
        print(len(news), "news articles about Apple fetched.")
        print(news)
    except Exception as e:
        print("Error fetching news:", e)

