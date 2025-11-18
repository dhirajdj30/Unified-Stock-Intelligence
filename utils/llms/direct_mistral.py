import requests

class DirectMistral:
    def __init__(self, config, max_tokens=512, temperature=0.0):
        self.config = config
        self.max_tokens = max_tokens
        self.temperature = temperature

    def invoke(self, prompt: str):
        payload = {
            "model": self.config.model_name,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": self.max_tokens,
            "temperature": self.temperature
        }

        r = requests.post(
            f"{self.config.url}/chat/completions",
            headers={
                "Authorization": f"Bearer {self.config.api_key}",
                "Content-Type": "application/json"
            },
            json=payload
        )

        data = r.json()
        return data["choices"][0]["message"]["content"]


