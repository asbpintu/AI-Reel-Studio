from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseModel


class Video(BaseModel):

    __tablename__ = "Videos"

    video_id: Mapped[int] = mapped_column(
        "VideoId",
        primary_key=True,
        autoincrement=True,
    )

    script_id: Mapped[int] = mapped_column(
        "ScriptId",
        ForeignKey("Scripts.ScriptId"),
        unique=True,
    )

    video_url: Mapped[str | None] = mapped_column(
        "VideoUrl",
        nullable=True,
    )

    status: Mapped[str] = mapped_column(
        "Status",
        default="PENDING",
    )

    duration_seconds: Mapped[int | None] = mapped_column(
        "DurationSeconds",
        nullable=True,
    )

    script = relationship(
        "Script",
        back_populates="video",
    )