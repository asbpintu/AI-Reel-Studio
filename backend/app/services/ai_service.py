from typing import Protocol


class AIProvider(Protocol):
    def generate_script(self, prompt: str) -> str:
        ...


class MockAIService:
    """
    Temporary AI service.

    Later this will be replaced with OpenAI/Gemini
    without changing ScriptService.
    """

    def generate_script(self, prompt: str) -> str:

        return f"""
HOOK:
Did you know India's history spans over 5000 years?

BODY:
This script was generated from the following prompt:

{prompt}

The story should begin with an engaging hook,
continue with educational storytelling,
and finish with a call to action.

ENDING:
Follow for more history videos.
"""