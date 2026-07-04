from pydantic import BaseModel
from pydantic import ConfigDict


class SceneCreate(BaseModel):

    scene_number: int
    narration: str
    image_prompt: str
    duration_seconds: int


class SceneResponse(BaseModel):

    scene_id: int
    scene_number: int
    narration: str
    image_prompt: str
    duration_seconds: int

    image_url: str | None = None
    image_status: str

    model_config = ConfigDict(
        from_attributes=True
    )