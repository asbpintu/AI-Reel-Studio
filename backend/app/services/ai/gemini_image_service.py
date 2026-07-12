from pathlib import Path
from google import genai


class GeminiImageService:

    def __init__(self, api_key: str):

        self.client = genai.Client(
            api_key=api_key
        )

    def generate_image(
        self,
        prompt: str,
        output_path: Path,
    ) -> Path:

        response = self.client.models.generate_images(
            model="gemini-2.5-flash-image-preview",
            prompt=prompt,
        )

        # Validate response structure to avoid 'None' subscriptable errors
        generated = getattr(response, "generated_images", None)
        if not generated or not isinstance(generated, (list, tuple)):
            raise ValueError("No generated images returned from the API")

        first = generated[0]
        if first is None:
            raise ValueError("First generated image is None")

        image = getattr(first, "image", None)
        if image is None:
            raise ValueError("Generated image object has no 'image' attribute or it is None")

        # If image has a save method (e.g., PIL Image-like), use it; otherwise, try writing raw bytes
        if hasattr(image, "save"):
            image.save(output_path)
        else:
            # assume image is bytes-like
            with open(output_path, "wb") as f:
                f.write(image)

        return output_path