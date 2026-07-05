from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.auth import get_current_user
from app.dependencies.database import get_db

from app.models.user import User

from app.schemas.scene import (
    SceneResponse, 
    SceneCreate
    )
from app.services.scene_service import SceneService

router = APIRouter(
    prefix="/scenes",
    tags=["Scenes"],
)


@router.post(
    "/{script_public_id}/generate-scenes",
    response_model=list[SceneResponse],
)
def generate_scenes(
    script_public_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    service = SceneService(db)

    return service.generate_scenes(
        script_public_id,
        current_user,
    )


@router.post(
    "/{scene_public_id}/generate-image",
    response_model=SceneResponse,
)
def generate_image(
    scene_public_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = SceneService(db)

    return service.generate_image(scene_public_id)

@router.post(
    "/{scene_public_id}/generate-audio",
    response_model=SceneResponse,
)
def generate_audio(
    scene_public_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = SceneService(db)

    return service.generate_audio(scene_public_id, current_user)