from PIL import Image, ImageDraw

import os
import uuid


class ImageService:

    def generate(self, prompt: str):

        os.makedirs("media/images", exist_ok=True)

        filename = f"{uuid.uuid4()}.png"

        filepath = os.path.join(
            "media/images",
            filename
        )

        image = Image.new(
            "RGB",
            (1024, 1024),
            color=(30, 30, 30)
        )

        draw = ImageDraw.Draw(image)

        draw.text(
            (40, 40),
            prompt[:250],
            fill="white"
        )

        image.save(filepath)

        return filepath