from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.auth import get_current_user
from app.dependencies.database import get_db

from app.models.user import User

from app.schemas.scene import SceneResponse

from app.services.scene_service import SceneService

router = APIRouter(
    prefix="/audio",
    tags=["Audio"],
)


@router.post(
    "/scripts/{script_public_id}/generate-audios",
    response_model=list[SceneResponse],
)
def generate_audios(
    script_public_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    service = SceneService(db)

    return service.generate_audios(
        script_public_id,
        current_user,
    )