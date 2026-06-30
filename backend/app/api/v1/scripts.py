from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.auth import get_current_user
from app.dependencies.database import get_db

from app.models.user import User

from app.schemas.script import (
    ScriptCreate,
    ScriptUpdate,
    ScriptResponse,
)

from app.services.script_service import ScriptService

router = APIRouter(
    prefix="/scripts",
    tags=["Scripts"],
)


@router.post(
    "/projects/{project_public_id}",
    response_model=ScriptResponse,
    status_code=201,
)
def create_script(
    project_public_id: str,
    request: ScriptCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = ScriptService(db)

    return service.create_script(
        project_public_id,
        request,
        current_user,
    )


@router.get(
    "/projects/{project_public_id}",
    response_model=list[ScriptResponse],
)
def list_scripts(
    project_public_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = ScriptService(db)

    return service.list_scripts(
        project_public_id,
        current_user,
    )


@router.get(
    "/{public_id}",
    response_model=ScriptResponse,
)
def get_script(
    public_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = ScriptService(db)

    return service.get_script(
        public_id,
        current_user,
    )


@router.put(
    "/{public_id}",
    response_model=ScriptResponse,
)
def update_script(
    public_id: str,
    request: ScriptUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = ScriptService(db)

    return service.update_script(
        public_id,
        request,
        current_user,
    )


@router.delete(
    "/{public_id}",
    status_code=204,
)
def delete_script(
    public_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = ScriptService(db)

    service.delete_script(
        public_id,
        current_user,
    )