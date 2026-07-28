from abc import ABC, abstractmethod




class BaseProvider(ABC):

    @abstractmethod
    def generate(self, prompt, model):
        pass

    # NEW
    def generate_stream(self, prompt, model):
        """
        Optional streaming support.

        Default implementation falls back
        to normal generation.
        """
        yield self.generate(prompt, model)

    @abstractmethod
    def health_check(self):
        """Check provider availability."""
        pass