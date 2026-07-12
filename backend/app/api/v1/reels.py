from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.dependencies.auth import get_current_user
from app.dependencies.database import get_db
from app.models.user import User
from app.schemas.reel import ReelCreate, ReelResponse
from app.services.reel_service import ReelService
from app.repositories.project_repository import ProjectRepository
from fastapi import HTTPException

router = APIRouter(
    prefix="/reels",
    tags=["Reels"],
)

@router.post(
    "/projects/{project_public_id}",
    response_model=ReelResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_reel(
    project_public_id: str,
    request: ReelCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    project_repository = ProjectRepository(db)
    project = project_repository.get_by_public_id(project_public_id)

    if project is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found",
        )

    if project.user_id != current_user.user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied",
        )

    service = ReelService(db)
    return service.create_reel(
        project_id=project.project_id,
        title=request.title,
        prompt=request.prompt,
    )

@router.get(
    "/projects/{project_public_id}",
    response_model=list[ReelResponse],
)
def list_reels(
    project_public_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    project_repository = ProjectRepository(db)
    project = project_repository.get_by_public_id(project_public_id)

    if project is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found",
        )

    if project.user_id != current_user.user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied",
        )

    service = ReelService(db)
    return service.list_reels(project.project_id)
