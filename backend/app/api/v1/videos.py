from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter

from app.dependencies.database import get_db
from app.dependencies.auth import get_current_user

from app.models.user import User

from app.services.video_service import VideoService

router = APIRouter(
    prefix="/video",
    tags=["Video"],
)

@router.post(
    "/scene/{scene_public_id}",
)
def generate_scene_video(
    scene_public_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    service = VideoService(db)

    return service.generate_scene_video(
        scene_public_id,
        current_user,
    )


@router.post(
    "/scripts/{script_public_id}/generate-videos",
)
def generate_videos(
    script_public_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    service = VideoService(db)

    return service.generate_videos(
        script_public_id,
        current_user,
    )


@router.post(
    "/script/{script_public_id}",
)
def generate_final_video(
    script_public_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    service = VideoService(db)

    return service.generate_final_video(
        script_public_id
    )