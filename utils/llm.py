from config.configs import get_mistral_config, get_gemini_config
from utils.llms.direct_mistral import DirectMistral
from utils.llms.direct_gemini import DirectGemini


def get_llm(provider: str, max_tokens=512, temperature=0.0):
    """
    provider: "mistral", "gemini"
    """

    provider = provider.lower()

    if provider == "mistral":
        config = get_mistral_config()
        return DirectMistral(config, max_tokens, temperature)

    elif provider == "gemini":
        config = get_gemini_config()
        return DirectGemini(config, max_tokens, temperature)

    else:
        raise ValueError(f"Unknown provider: {provider}")


if __name__ == "__main__":
    # llm = get_llm("mistral", max_tokens=100, temperature=0.7)
    # response = llm.invoke("Explain the theory of relativity in simple terms.")
    # print("Mistral Response:", response)

    llm = get_llm("gemini", max_tokens=100, temperature=0.7)
    response = llm.invoke("Capital of France.")
    print("Gemini Response:", response)