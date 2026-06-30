from sqlalchemy.orm import Session

from app.models.reel import Reel


class ReelRepository:

    def __init__(self, db: Session):

        self.db = db

    def create(self, reel: Reel):

        self.db.add(reel)

        self.db.commit()

        self.db.refresh(reel)

        return reel

    def get_by_project(self, project_id: int):

        return (
            self.db.query(Reel)
            .filter(Reel.project_id == project_id)
            .all()
        )