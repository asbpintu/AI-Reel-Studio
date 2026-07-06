from sqlalchemy.orm import Session
from pathlib import Path
import subprocess

from app.repositories.video_repository import VideoRepository
from app.repositories.script_repository import ScriptRepository
from app.repositories.scene_repository import SceneRepository
from app.models.video import Video
from app.models.scene import Scene
from app.services.ffmpeg_service import FFmpegService
from app.utils.media_helper import get_script_folder

from fastapi import HTTPException
from fastapi.responses import FileResponse



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
            media_type="videos",
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
                "video_path": str(filepath),
                "video_url": f"/media/videos/{script.public_id}/{filename}"
        }
    
    def generate_final_video(
        self,
        script_public_id: str,
    ):
        script = self.script_repository.get_by_public_id(
            script_public_id
        )

        if script is None:
            raise HTTPException(
                status_code=404,
                detail="Script not found."
            )
        
        scenes = self.scene_repository.list_by_script(script.script_id)

        if not scenes:
            raise HTTPException(
                status_code=400,
                detail="No scene videos found."
            )
        
        folder = get_script_folder(
            "videos",
            script_public_id
        )

        concat_file = folder / "concat.txt"

        with open(concat_file, "w", encoding="utf-8") as f:

            for scene in scenes:

                scene_video = (folder / f"scene_{scene.scene_number:02d}.mp4")

                if not scene_video.exists():
                    raise HTTPException(
                        status_code=400,
                        detail=f"Scene {scene.scene_number} video not generated."
                    )

                f.write(
                    f"file '{Path(scene_video).resolve()}'\n"
                )

        final_video_path = folder / "final_video.mp4"

        subprocess.run(

            [
                "ffmpeg",
                "-y",
                "-f",
                "concat",
                "-safe",
                "0",
                "-i",
                str(concat_file),
                "-c",
                "copy",
                str(final_video_path),
            ],

            check=True,
        )

        return {
            "message": "Final video created successfully.",
            "video_url": f"/media/videos/{script_public_id}/final_video.mp4"
        }
    

    def generate_videos(
        self,
        script_public_id: str,
        current_user,
    ):
        script = self.script_repository.get_by_public_id(
            script_public_id
        )

        if script is None:
            raise HTTPException(
                status_code=404,
                detail="Script not found.",
            )

        if script.project.user_id != current_user.user_id:
            raise HTTPException(
                status_code=403,
                detail="Access denied.",
            )

        scenes = self.scene_repository.list_by_script(
            script.script_id
        )

        if not scenes:
            raise HTTPException(
                status_code=404,
                detail="No scenes found.",
            )

        videos = []

        for scene in scenes:

            result = self.generate_scene_video(
                scene.public_id,
                current_user,
            )

            videos.append(
                {
                    "scene_number": scene.scene_number,
                    "video_path": result["video_path"],
                }
            )

        return videos
    

    def download_final_video(
        self,
        script_public_id: str,
        current_user,
    ):
        script = self.script_repository.get_by_public_id(
            script_public_id
        )

        if script is None:
            raise HTTPException(
                status_code=404,
                detail="Script not found.",
            )

        if script.project.user_id != current_user.user_id:
            raise HTTPException(
                status_code=403,
                detail="Access denied.",
            )

        folder = get_script_folder(
            media_type="videos",
            script_public_id=script_public_id,
        )

        final_video = folder / "final_video.mp4"

        if not final_video.exists():
            raise HTTPException(
                status_code=404,
                detail="Final video not found.",
            )

        return FileResponse(
            path=str(final_video),
            media_type="video/mp4",
            filename=f"{script_public_id}.mp4",
        )