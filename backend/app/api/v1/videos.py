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