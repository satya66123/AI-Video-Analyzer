from abc import ABC, abstractmethod


class BaseProvider(ABC):
    """
    Abstract base class for all AI providers.
    """

    @abstractmethod
    def get_models(self):
        """Return available models."""
        pass

    @abstractmethod
    def generate(self,model:str, prompt: str):
        """Generate AI response."""
        pass

    @abstractmethod
    def health_check(self):
        """Check provider availability."""
        pass