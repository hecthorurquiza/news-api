from .news_api_handler import NewsApiHandler

def test_get_news():
	news_api_handler = NewsApiHandler()
	tokens = ["Thrump", "Moraes"]

	articles = news_api_handler.get_news(tokens)

	assert articles is not None
	assert len(articles) > 0
	assert type(articles[0]) is dict 