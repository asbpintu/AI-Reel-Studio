from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base_model import BaseModel


class Reel(BaseModel):

    __tablename__ = "Reels"

    reel_id: Mapped[int] = mapped_column(
        "ReelId",
        primary_key=True,
        autoincrement=True,
    )

    project_id: Mapped[int] = mapped_column(
        "ProjectId",
        ForeignKey("Projects.ProjectId"),
    )

    title: Mapped[str] = mapped_column(
        "Title",
        String(200),
    )

    prompt: Mapped[str] = mapped_column(
        "Prompt",
        String(3000),
    )

    status: Mapped[str] = mapped_column(
        "Status",
        String(50),
        default="Pending",
    )

    project = relationship(
        "Project",
        back_populates="reels",
    )