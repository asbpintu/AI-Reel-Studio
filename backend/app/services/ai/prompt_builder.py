class PromptBuilder:

    @staticmethod
    def build_script_prompt(
        prompt: str,
        keywords: str | None = None,
        duration_seconds: int | None = None,
        language: str | None = None,
        reel_type: str | None = None,
        voice_type: str | None = None,
        style: str | None = None,
    ) -> str:

        extra_requirements = []

        if language:
            extra_requirements.append(f"Language: {language}")

        if duration_seconds:
            extra_requirements.append(f"Duration: {duration_seconds} seconds")

        if reel_type:
            extra_requirements.append(f"Reel type: {reel_type}")

        if voice_type:
            extra_requirements.append(f"Voice type: {voice_type}")

        if style:
            extra_requirements.append(f"Style: {style}")

        if keywords:
            extra_requirements.append(f"Focus keywords: {keywords}")

        requirements_text = "\n".join(extra_requirements)

        return f"""
    You are an expert Instagram Reel script writer.

    Write a highly engaging script.

    Requirements:

    - Hook in first sentence
    - Easy to understand
    - Maximum 60 seconds
    - Conversational
    - Add a CTA at the end
    {requirements_text}

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