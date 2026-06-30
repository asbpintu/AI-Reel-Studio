from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.dependencies.auth import get_current_user
from app.dependencies.database import get_db
from app.models.user import User
from app.repositories.project_repository import ProjectRepository
from app.schemas.project import (
    ProjectCreate,
    ProjectResponse,
    ProjectUpdate,
)
from app.services.project_service import ProjectService

router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
)


@router.post(
    "",
    response_model=ProjectResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_project(
    request: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    repository = ProjectRepository(db)
    service = ProjectService(repository)

    return service.create_project(
        request,
        current_user,
    )


@router.get(
    "",
    response_model=list[ProjectResponse],
)
def get_my_projects(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    repository = ProjectRepository(db)
    service = ProjectService(repository)

    return service.get_my_projects(current_user)


@router.get(
    "/{public_id}",
    response_model=ProjectResponse,
)
def get_project(
    public_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    repository = ProjectRepository(db)
    service = ProjectService(repository)

    return service.get_project(public_id)


@router.put(
    "/{public_id}",
    response_model=ProjectResponse,
)
def update_project(
    public_id: str,
    request: ProjectUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    repository = ProjectRepository(db)
    service = ProjectService(repository)

    return service.update_project(
        public_id,
        request,
    )


@router.delete(
    "/{public_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_project(
    public_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    repository = ProjectRepository(db)
    service = ProjectService(repository)

    service.delete_project(public_id)

    return None