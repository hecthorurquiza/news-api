import os
import requests

from .interfaces.news_api_handler_interface import INewsApiHandler

class NewsApiHandler(INewsApiHandler):
    def __init__(self) -> None:
        self.__api_key = os.getenv("NEWS_API_KEY")

    def get_news(self, tokens: list[str]) -> list[dict]:
        articles = []

        for token in tokens:
            url = f"https://newsapi.org/v2/everything?q={token}&language=pt&sortBy=relevancy&pageSize=3&apiKey={self.__api_key}"
            resp = requests.get(url)
            articles.extend(resp.json().get("articles"))

        return articles
