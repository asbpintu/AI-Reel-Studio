class PromptBuilder:

    @staticmethod
    def build_script_prompt(prompt: str) -> str:

        return f"""
You are an expert Instagram Reel script writer.

Write a highly engaging script.

Requirements:

- Hook in first sentence
- Easy to understand
- Maximum 60 seconds
- Conversational
- Add a CTA at the end

Topic:

{prompt}
"""