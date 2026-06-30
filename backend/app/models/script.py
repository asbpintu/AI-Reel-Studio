from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseModel

import uuid


class Script(BaseModel):

    __tablename__ = "Scripts"

    script_id: Mapped[int] = mapped_column(
        "ScriptId",
        primary_key=True,
        autoincrement=True,
    )

    public_id: Mapped[str] = mapped_column(
        "PublicId",
        String(36),
        default=lambda: str(uuid.uuid4()),
        unique=True,
        nullable=False,
        index=True,
    )

    project_id: Mapped[int] = mapped_column(
        "ProjectId",
        ForeignKey("Projects.ProjectId"),
    )

    prompt: Mapped[str] = mapped_column(
        "Prompt",
    )

    generated_script: Mapped[str | None] = mapped_column(
        "GeneratedScript",
    )

    status: Mapped[str] = mapped_column(
        "Status",
        String(50),
        default="Pending",
    )

    project = relationship(
        "Project",
        back_populates="scripts",
    )