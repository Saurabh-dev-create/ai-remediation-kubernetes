import os

from openai import OpenAI
from dotenv import load_dotenv

from analyzer_agent.providers.base import LLMProvider

load_dotenv()


class OpenAIProvider(LLMProvider):

    def __init__(self):

        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

    def analyze(self, prompt):

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a Kubernetes SRE expert."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        return response.choices[0].message.content