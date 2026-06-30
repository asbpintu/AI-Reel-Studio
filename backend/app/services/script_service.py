from fastapi import HTTPException, status

from app.models.script import Script
from app.repositories.script_repository import ScriptRepository
from app.repositories.project_repository import ProjectRepository
from app.schemas.script import ScriptCreate, ScriptUpdate


class ScriptService:

    def __init__(self, db):
        self.script_repository = ScriptRepository(db)
        self.project_repository = ProjectRepository(db)

    def create_script(
        self,
        project_public_id: str,
        request: ScriptCreate,
        current_user,
    ):
        project = self.project_repository.get_by_public_id(
            project_public_id
        )

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

        script = Script(
            project_id=project.project_id,
            prompt=request.prompt,
            generated_script=None,
            status="Pending",
        )

        return self.script_repository.create(script)

    def get_script(
        self,
        public_id: str,
        current_user,
    ):
        script = self.script_repository.get_by_public_id(
            public_id
        )

        if script is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Script not found",
            )
        if script.project.user_id != current_user.user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access denied",
            )

        return script

    def list_scripts(
        self,
        project_public_id: str,
        current_user,
    ):
        project = self.project_repository.get_by_public_id(
            project_public_id
        )

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

        return self.script_repository.get_by_project(
            project.project_id
        )

    def update_script(
        self,
        public_id: str,
        request: ScriptUpdate,
        current_user,
    ):
        script = self.get_script(public_id, current_user)

        if script.project.user_id != current_user.user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access denied",
            )

        if request.prompt is not None:
            script.prompt = request.prompt

        if request.generated_script is not None:
            script.generated_script = request.generated_script

        if request.status is not None:
            script.status = request.status

        self.script_repository.update(script)

        return script

    def delete_script(
        self,
        public_id: str,
        current_user,
    ):
        script = self.get_script(public_id, current_user)

        if script.project.user_id != current_user.user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access denied",
            )

        self.script_repository.delete(script)