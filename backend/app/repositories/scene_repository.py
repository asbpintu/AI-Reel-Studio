from sqlalchemy.orm import Session

from app.models.scene import Scene


class SceneRepository:

    def __init__(self, db: Session):

        self.db = db

    def create(self, scene: Scene):

        self.db.add(scene)

        self.db.flush()

        self.db.refresh(scene)

        return scene

    def create_many(self, scenes: list[Scene]):

        self.db.add_all(scenes)

        self.db.flush()

        return scenes

    def get_by_reel(self, reel_id: int):

        return (
            self.db.query(Scene)
            .filter(Scene.reel_id == reel_id)
            .order_by(Scene.scene_number)
            .all()
        )