import google.generativeai as genai

from app.core.config import get_settings
from app.services.ai.base_llm_service import BaseLLMService


settings = get_settings()

genai.configure(api_key=settings.GEMINI_API_KEY)


class GeminiService(BaseLLMService):

    def __init__(self):
        self.model = genai.GenerativeModel(
            model_name="gemini-2.5-flash"
        )

    def generate_text(self, prompt: str) -> str:

        response = self.model.generate_content(prompt)

        return response.text