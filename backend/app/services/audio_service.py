import time

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
        scene_id: int,
        narration: str,
    ) -> str:
        
        filename = f"scene_{scene_id:02d}.mp3"
        folder = get_script_folder(
            media_type="audios",
            script_public_id=script_public_id
        )
        filepath = folder / filename

        time.sleep(1)
        
        return str(filepath)