from sqlalchemy.orm import Session

from app.models.scene import Scene
from app.repositories.scene_repository import SceneRepository


class SceneService:

    def __init__(self, db: Session):

        self.repository = SceneRepository(db)

    def create_scene(
        self,
        reel_id: int,
        scene_number: int,
        narration: str,
        image_prompt: str,
        video_prompt: str,
        duration: int,
    ):

        try:

            scene = Scene(
                reel_id=reel_id,
                scene_number=scene_number,
                narration=narration,
                image_prompt=image_prompt,
                video_prompt=video_prompt,
                duration=duration,
                status="Pending",
            )

            scene = self.repository.create(scene)

            self.repository.db.commit()

            return scene

        except Exception:

            self.repository.db.rollback()
            raise

    def get_scenes(
        self,
        reel_id: int,
    ):

        return self.repository.get_by_reel(reel_id)