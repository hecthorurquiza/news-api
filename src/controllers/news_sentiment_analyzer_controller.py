from datetime import datetime as dt

from .interfaces.news_sentiment_analyzer_controller_interface import INewsSentimentAnalyzerController
from src.provider.interfaces.news_api_handler_interface import INewsApiHandler
from src.provider.interfaces.gemini_api_handler_interface import IGeminiApiHandler
from src.provider.interfaces.feeling_model_handler_interface import IFeelingModelHandler

class NewsSentimentAnalyzerController(INewsSentimentAnalyzerController):
    
    def __init__(
            self, news_api_handler: INewsApiHandler, 
            gemini_api_handler: IGeminiApiHandler, feeling_model_handler: IFeelingModelHandler
        ) -> None:
        self.__news_api_handler = news_api_handler
        self.__gemini_api_handler = gemini_api_handler
        self.__feeling_model_handler = feeling_model_handler
    
    def analyze_news(self, tokens: list[str]) -> dict:
        articles = self.__news_api_handler.get_news(tokens)
        feeling_scores = []

        for article in articles:
            shortened_text = self.__gemini_api_handler.shorten_with_gemini(article.get("content"))
            feeling_scores.append(self.__feeling_model_handler.analyze_feeling(shortened_text))

        mean_score = sum(item["score"] for item in feeling_scores) / len(feeling_scores)
        most_common_label = max(
            set(item["label"] for item in feeling_scores), 
            key=lambda x: sum(1 for item in feeling_scores if item["label"] == x)
        )
        feeling_data = { "mean_score": mean_score, "most_common_label": most_common_label }

        return self.__formatted_response(articles, feeling_data)

    def __formatted_response(self, articles: list[dict], feeling_data: dict) -> dict:
        data = []

        for article in articles:
            str_date = article.get("publishedAt")
            str_date_aplitted = str_date.split("T")
            date_aplitted = str_date_aplitted[0].split("-")
            year = int(date_aplitted[0])
            month = int(date_aplitted[1])
            day = int(date_aplitted[2])
            formatted_date = dt(year, month, day).strftime("%d/%m/%Y")

            data.append({
                "title": article.get("title"),
                "description": article.get("description"),
                "url": article.get("url"),
                "urlToImage": article.get("urlToImage"),
                "publishedAt": formatted_date
            })

        return {
            "data": data,
            "feeling_data": feeling_data
        }