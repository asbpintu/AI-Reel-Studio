from pydantic import BaseModel
from pydantic import ConfigDict


class SceneCreate(BaseModel):

    scene_number: int
    narration: str
    image_prompt: str
    duration_seconds: int


class SceneResponse(BaseModel):

    scene_id: int
    public_id: str
    scene_number: int
    narration: str
    image_prompt: str
    duration_seconds: int

    image_url: str | None = None
    image_status: str

    audio_url: str | None = None
    audio_status: str | None = None

    model_config = ConfigDict(
        from_attributes=True
    )