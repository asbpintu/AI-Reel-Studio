from sqlalchemy.orm import Session

from app.models.script import Script


class ScriptRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, script: Script):
        self.db.add(script)
        self.db.commit()
        self.db.refresh(script)
        return script

    def get_by_public_id(self, public_id: str):
        return (
            self.db.query(Script)
            .filter(Script.public_id == public_id)
            .first()
        )

    def get_by_project(self, project_id: int):
        return (
            self.db.query(Script)
            .filter(Script.project_id == project_id)
            .all()
        )

    def update(self, script):
        self.db.commit()
        self.db.refresh(script)
        return script

    def delete(self, script: Script):
        self.db.delete(script)
        self.db.commit()