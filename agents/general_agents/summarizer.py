from utils.llm import get_llm 


def summarize_news_article(article_texts: list, provider: str = "gemini") -> str:
    """ Summarize a news article using the specified LLM provider. """
    
    article_text = ""
    for article in article_texts:
        article_text = article_text + article.strip() + " "
    llm = get_llm(provider, max_tokens=150, temperature=0.5)
    prompt = f"Summarize the following news article in a concise manner:\n\n{article_text}"
    summary = llm.invoke(prompt)
    return summary


if __name__ == "__main__":
    sample_article = [
        "Scientists have discovered a new exoplanet that could potentially support life. ",
        "The planet, named Kepler-1649c, is located in the habitable zone of its star, ",
        "where conditions may be right for liquid water to exist. This discovery was made ",
        "using data from NASA's Kepler space telescope. Researchers are excited about the ",
        "possibility of finding signs of life on this distant world.",
    ]
    
    summary = summarize_news_article(sample_article, provider="gemini")
    print("Article Summary:", summary)