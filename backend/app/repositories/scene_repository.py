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
    
    def list_by_script(self, script_id: int):

        return (
            self.db.query(Scene)
            .filter(Scene.script_id == script_id)
            .order_by(Scene.scene_number)
            .all()
        )
    
    def delete_by_script(self, script_id: int):

        self.db.query(Scene).filter(Scene.script_id == script_id).delete()

    def update(self, scene: Scene):

        self.db.add(scene)
        self.db.flush()
        self.db.refresh(scene)

        return scene
    
    def get_by_public_id(
        self,
        public_id: str,
    ):

        return (
            self.db.query(Scene)
            .filter(Scene.public_id == public_id)
            .first()
        )
    
    def get_by_script_id(self, script_id: int):

        return (
            self.db.query(Scene)
            .filter(Scene.script_id == script_id)
            .order_by(Scene.scene_number)
            .all()
        )