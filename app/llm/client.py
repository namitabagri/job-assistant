from openai import OpenAI

from config.settings import (
    OPENAI_API_KEY,
    OPENAI_MODEL,
)


class LLMClient:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.model = OPENAI_MODEL

    def generate(self, prompt: str) -> str:
        response = self.client.responses.create(
            model=self.model,
            input=prompt,
        )

        return response.output_text