from abc import ABC, abstractmethod

class INewsApiHandler(ABC):

    @abstractmethod
    def get_news(self, tokens: list) -> list[dict]:
        pass