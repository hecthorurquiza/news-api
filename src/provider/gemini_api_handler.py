import os
import google.generativeai as genai

from .interfaces.gemini_api_handler_interface import IGeminiApiHandler

class GeminiApiHandler(IGeminiApiHandler):
    def __init__(self):
        self.__api_key = os.getenv("GEMINI_API_KEY")
        genai.configure(api_key=self.__api_key)
        self.__model = genai.GenerativeModel(model_name="gemini-1.5-flash-8b")

    def shorten_with_gemini(self, text: str) -> str:
        formatted_text = f"{text} \nSummarize the text in a single paragraph."
        response = self.__model.generate_content(formatted_text)
        return response.text
