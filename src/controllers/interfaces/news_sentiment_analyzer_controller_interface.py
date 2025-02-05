from abc import ABC, abstractmethod

class INewsSentimentAnalyzerController(ABC):

    @abstractmethod
    def analyze_news(tokens: list[str]) -> None:
        pass