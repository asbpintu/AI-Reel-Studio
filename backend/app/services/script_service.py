from fastapi import HTTPException, status

from app.models.script import Script
from app.repositories.script_repository import ScriptRepository
from app.repositories.project_repository import ProjectRepository
from app.schemas.script import ScriptCreate, ScriptUpdate
from app.services.ai.llm_factory import LLMFactory
from app.services.ai.prompt_builder import PromptBuilder

from app.constants.status import ScriptStatus

class ScriptService:

    def __init__(self, db):

        self.db = db
        self.script_repository = ScriptRepository(db)
        self.project_repository = ProjectRepository(db)
        self.ai_service = LLMFactory.create()
        self.prompt_builder = PromptBuilder()

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
            keywords=request.keywords,
            duration_seconds=request.duration_seconds,
            language=request.language,
            reel_type=request.reel_type,
            voice_type=request.voice_type,
            style=request.style,
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

        if request.keywords is not None:
            script.keywords = request.keywords

        if request.duration_seconds is not None:
            script.duration_seconds = request.duration_seconds

        if request.language is not None:
            script.language = request.language

        if request.reel_type is not None:
            script.reel_type = request.reel_type

        if request.voice_type is not None:
            script.voice_type = request.voice_type

        if request.style is not None:
            script.style = request.style

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

    def generate_script(
        self,
        script_public_id: str,
        current_user,
    ):

        script = self.script_repository.get_by_public_id(script_public_id)

        if script is None:
            raise HTTPException(
                status_code=404,
                detail="Script not found.",
            )

        project = script.project

        if project.user_id != current_user.user_id:
            raise HTTPException(
                status_code=403,
                detail="Access denied",
            )

        try:
            prompt = PromptBuilder.build_script_prompt(
                script.prompt,
                keywords=script.keywords,
                duration_seconds=script.duration_seconds,
                language=script.language,
                reel_type=script.reel_type,
                voice_type=script.voice_type,
                style=script.style,
            )

            generated_script = self.ai_service.generate_text(prompt)

            script.generated_script = generated_script
            script.status = ScriptStatus.SCRIPT_GENERATED
            self.script_repository.save(script)

        except Exception as ex:
            script.status = ScriptStatus.FAILED
            self.script_repository.save(script)

            raise HTTPException(
                status_code=500,
                detail=str(ex),
            )

        self.script_repository.save(script)

        return script