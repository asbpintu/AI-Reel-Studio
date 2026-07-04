from abc import ABC, abstractmethod


class BaseLLMService(ABC):

    @abstractmethod
    def generate_text(self, prompt: str) -> str:
        pass