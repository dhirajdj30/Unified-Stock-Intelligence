from agents.news_agents.realtime_news_agent import fetch_news_for_company
from agents.general_agents.summarizer import summarize_news_article

def main():
    print("Hello from unified-stock-intelligence!")
    ticker = "MSFT"
    news_articles = fetch_news_for_company(ticker, '2025-11-18', '2025-11-18')
    print(f"{len(news_articles)} news articles about {ticker} fetched.")
    articles = []
    for article in news_articles:

        article_title = article.get('headline', 'No Title')
        article_summary = article.get('summary', 'No Summary')
        articles.append(f"Title: {article_title} Summary: {article_summary}")

    print(type(articles))

    summary = summarize_news_article(
        article_texts=articles, provider="gemini"
    )
    print("Summary of selected articles:", summary)



if __name__ == "__main__":
    main()
