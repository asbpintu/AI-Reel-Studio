from sqlalchemy import ForeignKey, Integer, String

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseModel


class Scene(BaseModel):

    __tablename__ = "Scenes"

    scene_id: Mapped[int] = mapped_column(
        "SceneId",
        primary_key=True,
        autoincrement=True,
    )

    script_id: Mapped[int] = mapped_column(
        "ScriptId",
        ForeignKey("Scripts.ScriptId"),
    )

    scene_number: Mapped[int] = mapped_column(
        "SceneNumber",
    )

    narration: Mapped[str] = mapped_column(
        "Narration",
    )

    image_prompt: Mapped[str] = mapped_column(
        "ImagePrompt",
    )

    duration_seconds: Mapped[int] = mapped_column(
        "DurationSeconds",
        default=5,
    )

    image_url: Mapped[str | None] = mapped_column(
        "ImageUrl",
        nullable=True,
    )

    image_status: Mapped[str] = mapped_column(
        "ImageStatus",
        default="PENDING",
    )

    script = relationship(
        "Script",
        back_populates="scenes",
    )