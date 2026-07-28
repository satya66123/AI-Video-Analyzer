import os

from openai import OpenAI

from providers.base_provider import BaseProvider


class OpenAIProvider(BaseProvider):

    def __init__(self):

        self.api_key = os.getenv("OPENAI_API_KEY")

        self.client = OpenAI(api_key=self.api_key)

    def get_models(self):

        try:

            models = self.client.models.list()

            return sorted(
                [model.id for model in models.data]
            )

        except Exception:

            return []

    def generate(self,model, prompt):

        try:

            response = self.client.responses.create(
                model=model,
                input=prompt
            )

            return response.output_text

        except Exception as e:

            return f"Error: {str(e)}"

    def health_check(self):

        try:

            self.client.models.list()

            return True

        except Exception:

            return False