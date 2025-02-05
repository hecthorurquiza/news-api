from abc import ABC, abstractmethod

class IFeelingModelHandler(ABC):
    
    @abstractmethod
    def analyze_feeling(self, text: str) -> dict:
        pass