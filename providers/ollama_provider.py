import requests

from providers.base_provider import BaseProvider


class OllamaProvider(BaseProvider):

    BASE_URL = "http://localhost:11434"

    def get_models(self):

        try:
            response = requests.get(
                f"{self.BASE_URL}/api/tags",
                timeout=10
            )

            response.raise_for_status()

            return response.json()

        except Exception:
            return {}

    def generate(self, prompt, model):

        payload = {
            "model": model,
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(
            f"{self.BASE_URL}/api/generate",
            json=payload,
            timeout=300
        )

        response.raise_for_status()

        return response.json()["response"]

    def health_check(self):

        try:
            response = requests.get(
                self.BASE_URL,
                timeout=5
            )

            return response.status_code == 200

        except Exception:
            return False