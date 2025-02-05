from flask import Flask, jsonify, request
from dotenv import load_dotenv
from src.provider.news_api_handler import NewsApiHandler
from src.provider.gemini_api_handler import GeminiApiHandler
from src.provider.feeling_model_handler import FeelingModelHandler
from src.controllers.news_sentiment_analyzer_controller import NewsSentimentAnalyzerController

load_dotenv()

app = Flask(__name__)

@app.route('/search-news', methods=['GET'])
def search_news():
    tokens = request.args.get("tokens")
    invalid_separators = [';', '-', '_', '[', ']']

    if not tokens:
        return jsonify({"error": "Informe ao menos um token"}), 400
    
    if any(sep in tokens for sep in invalid_separators):
        return jsonify({"error": "Tokens devem ser separados por vírgula"}), 400

    news_handler = NewsApiHandler()
    gemini_handler = GeminiApiHandler()
    feeling_handler = FeelingModelHandler()
    news_controller = NewsSentimentAnalyzerController(news_handler, gemini_handler, feeling_handler)

    resp = news_controller.analyze_news(tokens.split(','))

    return jsonify(resp), 200