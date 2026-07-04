from app.services.ai.gemini_service import GeminiService


class LLMFactory:

    @staticmethod
    def get_llm():

        return GeminiService()