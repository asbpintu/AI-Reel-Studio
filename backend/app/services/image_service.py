from app.repositories.scene_repository import SceneRepository
from app.repositories.script_repository import ScriptRepository

from fastapi import HTTPException





class ImageService:

    def __init__(self, db):
        self.db = db
        self.scene_repository = SceneRepository(db)
        self.script_repository = ScriptRepository(db)

    def generate(self, prompt: str):

        print(prompt)

        return "https://dummyimage.com/1024x1024"