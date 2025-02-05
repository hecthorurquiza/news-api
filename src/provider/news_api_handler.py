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

    # def generate_csv(self, data: list[dict]) -> None:
    #     with tempfile.NamedTemporaryFile(mode='w', newline='', delete=False, suffix='.csv') as temp_file:
    #         csv_writer = csv.writer(temp_file)
    #         csv_writer.writerow(['Title', 'Description', 'URL', 'URLImage', 'Content'])
            
    #         for item in data:
    #             csv_writer.writerow(
    #                 [item.get("title"), item.get("description"), item.get("url"), item.get("urlToImage"), item.get("content")]
    #             )
            
    #         temp_file_path = temp_file.name
    #         print(f'Temporary CSV file created: {temp_file_path}')

        # with open(temp_file_path, mode='r') as read_file:
        #     csv_reader = csv.reader(read_file)
        #     next(csv_reader)  # Skip the header row
        #     for row in csv_reader:
        #         print(row[1])

        # os.remove(temp_file_path)
        # print(f'Temporary CSV file deleted: {temp_file_path}')
