
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.auth import get_current_user
from app.dependencies.database import get_db

from app.models.user import User

from app.services.image_service import ImageService
from app.schemas.scene import SceneResponse

router = APIRouter(
    prefix="/image",
    tags=["Image"],
)

@router.post(
    "/scripts/{script_public_id}/generate-all",
    response_model=list[SceneResponse],
)
def generate_all_images(
    script_public_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    service = ImageService(db)

    return service.generate_all_images_from_script(
        script_public_id,
        current_user,
    )