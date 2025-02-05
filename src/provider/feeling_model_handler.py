from transformers import pipeline

from .interfaces.feeling_model_handler_interface import IFeelingModelHandler

class FeelingModelHandler(IFeelingModelHandler):
    def __init__(self) -> None:
        self.__model_pipeline = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english",
            framework="pt"
        )

    def analyze_feeling(self, text: str) -> dict:
        result = self.__model_pipeline(text)
        return result[0]
    