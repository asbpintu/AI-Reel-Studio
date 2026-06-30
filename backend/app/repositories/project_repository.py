from sqlalchemy.orm import Session

from app.models.project import Project


class ProjectRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, project: Project):
        self.db.add(project)
        self.db.flush()
        self.db.refresh(project)
        return project

    def get_all_by_user(self, user_id: int):
        return (
            self.db.query(Project)
            .filter(Project.user_id == user_id)
            .all()
        )

    def get_by_public_id(self, public_id: str):
        return (
            self.db.query(Project)
            .filter(Project.public_id == public_id)
            .first()
        )
    
    def update(self, project):
        self.db.flush()
        self.db.refresh(project)
        return project

    def delete(self, project):

        self.db.delete(project)
        self.db.flush()