from pydantic import BaseModel
from pydantic import ConfigDict


class VideoResponse(BaseModel):

    video_id: int

    video_url: str | None

    status: str

    duration_seconds: int | None

    model_config = ConfigDict(
        from_attributes=True
    )