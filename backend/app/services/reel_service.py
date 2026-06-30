from sqlalchemy.orm import Session

from app.models.reel import Reel
from app.repositories.reel_repository import ReelRepository


class ReelService:

    def __init__(self, db: Session):

        self.repository = ReelRepository(db)

    def create_reel(
        self,
        project_id: int,
        title: str,
        prompt: str,
    ):

        reel = Reel(

            project_id=project_id,

            title=title,

            prompt=prompt,

            status="Pending",
        )

        return self.repository.create(reel)

    def list_reels(
        self,
        project_id: int,
    ):

        return self.repository.get_by_project(project_id)