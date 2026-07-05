import time

from app.repositories.script_repository import ScriptRepository
from app.repositories.scene_repository import SceneRepository


class AudioService:

    def __init__(self, db):
        self.db = db
        self.scene_repository = SceneRepository(db)
        self.script_repository = ScriptRepository(db)

    def generate(
        self,
        narration: str,
    ) -> str:

        print(f"Generating audio for: {narration}")

        time.sleep(1)

        return "https://dummyaudio.com/audio.mp3"