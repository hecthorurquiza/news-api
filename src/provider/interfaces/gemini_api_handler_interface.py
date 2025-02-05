from abc import ABC, abstractmethod

class IGeminiApiHandler(ABC):

    @abstractmethod
    def shorten_with_gemini(self, text: str) -> str:
        pass
