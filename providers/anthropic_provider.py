import os

import anthropic

from providers.base_provider import BaseProvider


class AnthropicProvider(BaseProvider):

    def __init__(self):

        self.api_key = os.getenv("ANTHROPIC_API_KEY")

        self.client = anthropic.Anthropic(
            api_key=self.api_key
        )

    def get_models(self):

        return [
            "claude-opus-4.1",
            "claude-sonnet-4",
            "claude-3.7-sonnet",
            "claude-3.5-sonnet",
            "claude-3.5-haiku"
        ]

    def generate(
        self,
        prompt,
        model,
        max_tokens=1024,
        temperature=0.7
    ):

        try:

            response = self.client.messages.create(

                model=model,

                max_tokens=max_tokens,

                temperature=temperature,

                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            return response.content[0].text

        except Exception as e:

            return f"Error: {str(e)}"

    def health_check(self):

        try:

            self.client.messages.create(

                model="claude-3.5-haiku",

                max_tokens=10,

                messages=[
                    {
                        "role": "user",
                        "content": "Hello"
                    }
                ]
            )

            return True

        except Exception:

            return False