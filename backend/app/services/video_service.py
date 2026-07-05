from sqlalchemy.orm import Session
from pathlib import Path

from app.repositories.video_repository import VideoRepository
from app.repositories.script_repository import ScriptRepository
from app.repositories.scene_repository import SceneRepository
from app.models.video import Video
from app.models.scene import Scene
from app.services.ffmpeg_service import FFmpegService
from app.utils.media_helper import get_script_folder

from fastapi import HTTPException



class VideoService:

    def __init__(self, db: Session):

        self.db = db

        self.video_repository = VideoRepository(db)
        self.scene_repository = SceneRepository(db)
        self.script_repository = ScriptRepository(db)
        self.ffmpeg_service = FFmpegService()

    def generate_scene_video(
        self,
        scene_public_id: str,
        current_user,
    ):
        scene = self.scene_repository.get_by_public_id(scene_public_id)

        if scene is None:
            raise HTTPException(
                status_code=404,
                detail="Scene not found.",
            )
        
        script = scene.script

        if script.project.user_id != current_user.user_id:  
            raise HTTPException(
                status_code=403,
                detail="Access denied.",
            )
        
        if not scene.image_url:
            raise HTTPException(
                status_code=400,
                detail="Scene image not generated.",
            )
        
        if not scene.audio_url:
            raise HTTPException(
                status_code=400,
                detail="Scene audio not generated.",
            )
        
        filename = f"scene_{scene.scene_number:02d}.mp4"
        folder = get_script_folder(
            media_type="images",
            script_public_id=script.public_id
        )

        filepath = folder / filename

        self.ffmpeg_service.create_scene_video(
            scene.image_url,
            scene.audio_url,
            str(filepath)
        )

        return {
                "message": "Video created successfully.",
                "video_path": str(filepath)
        }