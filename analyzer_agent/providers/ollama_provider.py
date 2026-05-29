import requests
from analyzer_agent.providers.base import LLMProvider


class OllamaProvider(LLMProvider):

    def analyze(self, prompt):

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3:latest",
                "prompt": prompt,
                "stream": False
            }
        )

        data = response.json()

        if "response" in data:
            return data["response"]

        print("Raw response:", data)
        return "❌ No valid response from Ollama."