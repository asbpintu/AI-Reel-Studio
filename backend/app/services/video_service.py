from sqlalchemy.orm import Session

from app.repositories.video_repository import VideoRepository
from app.repositories.script_repository import ScriptRepository
from app.services.ffmpeg_service import FFmpegService


class VideoService:

    def __init__(self, db: Session):

        self.db = db

        self.video_repository = VideoRepository(db)

        self.script_repository = ScriptRepository(db)
        self.ffmpeg_service = FFmpegService()

    def generate_scene_video(
        self,
        scene_public_id: str,
        current_user,
    ):
        # Fetch the scene and script based on the provided scene_public_id
        pass