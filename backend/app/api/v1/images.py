
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.auth import get_current_user
from app.dependencies.database import get_db

from app.models.user import User

from app.services.scene_service import SceneService
from app.schemas.scene import SceneResponse
import os
import tempfile
from pathlib import Path

from app.services.ai.gemini_image_service import GeminiImageService

router = APIRouter(
    prefix="/image",
    tags=["Image"],
)


@router.post(
    "/scripts/{script_public_id}/generate-images",
    response_model=list[SceneResponse],
)
def generate_images(
    script_public_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    service = SceneService(db)

    return service.generate_images(
        script_public_id,
        current_user,
    )


@router.get("/test-gemini")
def test_gemini():

    service = GeminiImageService(api_key=os.getenv("GEMINI_API_KEY", ""))

    # create a temporary file path for the generated image
    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png").name

    return {
        "response": service.generate_image(
            "Say Hello from Gemini.",
            output_path=Path(tmp_file),
        )
    }