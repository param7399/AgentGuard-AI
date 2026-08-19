from typing import Optional

from openai import OpenAI

from src.config.settings import (
    OPENAI_API_KEY,
    OPENAI_MODEL,
    AI_TEMPERATURE,
)


class AIClient:

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: Optional[str] = None,
    ):
        self.api_key = api_key or OPENAI_API_KEY
        self.model = model or OPENAI_MODEL

        self.client = None

        if self.api_key:
            self.client = OpenAI(
                api_key=self.api_key
            )

    @property
    def available(self) -> bool:
        return self.client is not None

    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = AI_TEMPERATURE,
    ) -> str:

        if not self.client:
            raise RuntimeError(
                "OpenAI API key is not configured."
            )

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=temperature,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ],
        )

        return response.choices[0].message.content or ""