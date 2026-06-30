from pydantic import BaseModel
from pydantic import ConfigDict


class ReelCreate(BaseModel):

    title: str

    prompt: str


class ReelResponse(BaseModel):

    reel_id: int

    title: str

    prompt: str

    status: str

    model_config = ConfigDict(
        from_attributes=True
    )