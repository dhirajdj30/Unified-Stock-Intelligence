from google import genai
from google.genai.types import GenerateContentConfig


class DirectGemini:
    """
    Lightweight official Gemini client.
    No LangChain. Supports gemini-2.5 models.
    """
    
    def __init__(self, config, max_tokens=512, temperature=0.0):
        self.model = config.model_name
        
        self.client = genai.Client(
            api_key=config.api_key
        )

        self.gen_config = GenerateContentConfig(
            max_output_tokens=max_tokens,
            temperature=temperature
        )

    def invoke(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=self.gen_config
        )

        # Extract the text from the official SDK
        try:
            return response.text
        except Exception:
            return str(response)

if __name__ == "__main__":
    from dotenv import load_dotenv
    from config.configs import LLMConfig
    import os

    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")

    config = LLMConfig(
        model_name="gemini-2.0-flash",  
        api_key=api_key
    )

    gemini = DirectGemini(config, max_tokens=100, temperature=0.7)
    response = gemini.invoke("Explain black holes in simple terms.")
    print("Gemini Response:", response)
