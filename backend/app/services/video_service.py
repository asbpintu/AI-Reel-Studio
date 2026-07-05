from sqlalchemy.orm import Session

from app.repositories.video_repository import VideoRepository
from app.repositories.script_repository import ScriptRepository


class VideoService:

    def __init__(self, db: Session):

        self.db = db

        self.video_repository = VideoRepository(db)

        self.script_repository = ScriptRepository(db)