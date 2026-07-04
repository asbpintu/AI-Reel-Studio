from urllib import response

from sqlalchemy.orm import Session

from app.repositories.scene_repository import SceneRepository
from app.repositories.script_repository import ScriptRepository

from app.services.ai.prompt_builder import PromptBuilder
from app.services.ai.llm_factory import LLMFactory

from app.models.scene import Scene
from fastapi import HTTPException

import json


class SceneService:

    def __init__(self, db: Session):

        self.db = db
        self.scene_repository = SceneRepository(db)
        self.script_repository = ScriptRepository(db)
        self.ai_service = LLMFactory.create()
        self.prompt_builder = PromptBuilder()
        

    def generate_scenes(
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
        
        if script.project.user_id != current_user.user_id:
            raise HTTPException(
                status_code=403,
                detail="Access denied.",
            )
        if not script.generated_script:
            raise HTTPException(
                status_code=400,
                detail="Generate the script first.",
            )
        prompt = PromptBuilder.build_scene_prompt(
            script.generated_script
        )
        response = self.ai_service.generate_text(prompt)

        try:
            scenes_data = json.loads(response)

        except Exception:
            raise HTTPException(
                status_code=500,
                detail="AI returned invalid JSON."
            )

        # Delete previous scenes
        self.scene_repository.delete_by_script(script.script_id)

        scenes = []

        for item in scenes_data:
            scene = Scene(
                script_id=script.script_id,
                scene_number=item["scene_number"],
                narration=item["narration"],
                image_prompt=item["image_prompt"],
                duration_seconds=item["duration_seconds"],
            )

            scenes.append(scene)

        self.scene_repository.create_many(scenes)
        self.db.commit()

        for scene in scenes:
            self.db.refresh(scene)

        return scenes