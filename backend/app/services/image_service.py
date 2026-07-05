from PIL import Image, ImageDraw
from app.utils.media_helper import get_script_folder


class ImageService:

    def generate(
            self,
            script_public_id: str,
            scene_id: int,
            prompt: str):

        filename = f"scene_{scene_id:02d}.png"
        folder = get_script_folder(
            media_type="images",
            script_public_id=script_public_id
        )

        filepath = folder / filename
        
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

        return str(filepath)