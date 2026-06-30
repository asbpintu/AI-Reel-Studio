from pydantic import BaseModel
from pydantic import ConfigDict


class SceneCreate(BaseModel):

    scene_number: int

    narration: str

    image_prompt: str

    video_prompt: str

    duration: int


class SceneResponse(BaseModel):

    scene_id: int

    scene_number: int

    narration: str

    image_prompt: str

    video_prompt: str

    duration: int

    status: str

    model_config = ConfigDict(
        from_attributes=True
    )