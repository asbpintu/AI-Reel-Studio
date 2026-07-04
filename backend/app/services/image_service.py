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
    
    def generate_all_images(
        self,
        script_id: int,
    ):
        scenes = self.scene_repository.list_by_script(script_id)

        generated = []

        for scene in scenes:

            image_url = "https://dummyimage.com/1024x1024"

            scene.image_url = image_url
            scene.image_status = "COMPLETED"

            generated.append(scene)

        self.db.commit()

        return generated
    
    def generate_all_images_from_script(
        self,
        script_public_id: str,
        current_user,
    ):
        script = self.script_repository.get_by_public_id(script_public_id)

        if script is None:
            raise HTTPException(status_code=404, detail="Script not found.")

        if script.project.user_id != current_user.user_id:
            raise HTTPException(status_code=403, detail="Access denied.")
        
        scenes = self.scene_repository.list_by_script(script.script_id)

        for scene in scenes:

            scene.image_url = "https://dummyimage.com/1024x1024"
            scene.image_status = "COMPLETED"

        self.db.commit()

        for scene in scenes:
            self.db.refresh(scene)

        return scenes