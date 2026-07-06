import subprocess

from app.repositories.script_repository import ScriptRepository
from app.repositories.scene_repository import SceneRepository
from app.utils.media_helper import get_script_folder


class AudioService:

    def __init__(self, db):
        self.db = db
        self.scene_repository = SceneRepository(db)
        self.script_repository = ScriptRepository(db)

    def generate(
        self,
        script_public_id: str,
        scene_number: int,
        narration: str,
    ):

        filename = f"scene_{scene_number:02d}.mp3"

        folder = get_script_folder(
            media_type="audios",
            script_public_id=script_public_id,
        )

        filepath = folder / filename

        subprocess.run(
            [
                "ffmpeg",
                "-f",
                "lavfi",
                "-i",
                "anullsrc=r=44100:cl=stereo",
                "-t",
                "5",
                "-q:a",
                "9",
                "-acodec",
                "libmp3lame",
                "-y",
                str(filepath),
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        return {"audio_url": f"/media/audios/{script_public_id}/{filename}"}