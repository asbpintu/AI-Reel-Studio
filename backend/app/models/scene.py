from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base_model import BaseModel


class Scene(BaseModel):

    __tablename__ = "Scenes"

    scene_id: Mapped[int] = mapped_column(
        "SceneId",
        primary_key=True,
        autoincrement=True,
    )

    reel_id: Mapped[int] = mapped_column(
        "ReelId",
        ForeignKey("Reels.ReelId"),
    )

    scene_number: Mapped[int] = mapped_column(
        "SceneNumber",
        Integer,
    )

    narration: Mapped[str] = mapped_column(
        "Narration",
        String(4000),
    )

    image_prompt: Mapped[str] = mapped_column(
        "ImagePrompt",
        String(4000),
    )

    video_prompt: Mapped[str] = mapped_column(
        "VideoPrompt",
        String(4000),
    )

    duration: Mapped[int] = mapped_column(
        "Duration",
    )

    status: Mapped[str] = mapped_column(
        "Status",
        String(50),
        default="Pending",
    )

    reel = relationship(
        "Reel",
        back_populates="scenes",
    )