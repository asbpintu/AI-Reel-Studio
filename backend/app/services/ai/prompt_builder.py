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
    
    @staticmethod
    def build_scene_prompt(script: str) -> str:

        return f"""
    You are an expert Instagram Reel scene creator.

    Create engaging scenes based on the following script.

    Return ONLY valid JSON.

    Do not wrap the response in markdown.

    Do not use ```json.

    Return a JSON array in this format:

    [
    {{
        "scene_number": 1,
        "narration": "...",
        "image_prompt": "...",
        "duration_seconds": 5
    }}
    ]

    Script:

    {script}
    """