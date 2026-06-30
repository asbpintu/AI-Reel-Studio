from fastapi import HTTPException, status

from app.models.project import Project
from app.repositories.project_repository import ProjectRepository
from app.schemas.project import (
    ProjectCreate,
    ProjectUpdate,
)


class ProjectService:

    def __init__(self, repository: ProjectRepository):
        self.repository = repository

    def create_project(
        self,
        request: ProjectCreate,
        current_user,
    ):

        project = Project(
            user_id=current_user.user_id,
            project_name=request.project_name,
            description=request.description,
        )

        return self.repository.create(project)

    def get_my_projects(self, current_user):

        return self.repository.get_all_by_user(
            current_user.user_id
        )

    def get_project(
        self,
        public_id: str,
    ):

        project = self.repository.get_by_public_id(
            public_id
        )

        if not project:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Project not found",
            )

        return project
    
    def update_project(
        self,
        public_id: str,
        request: ProjectUpdate,
    ):

        project = self.get_project(public_id)

        if request.project_name is not None:
            project.project_name = request.project_name

        if request.description is not None:
            project.description = request.description

        self.repository.update()

        return project


    def delete_project(
        self,
        public_id: str,
    ):

        project = self.get_project(public_id)

        self.repository.delete(project)