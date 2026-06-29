from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseModel


class Project(BaseModel):

    __tablename__ = "Projects"

    project_id: Mapped[int] = mapped_column(
        "ProjectId",
        primary_key=True,
        autoincrement=True,
    )

    user_id: Mapped[int] = mapped_column(
        "UserId",
        ForeignKey("Users.UserId"),
    )

    project_name: Mapped[str] = mapped_column(
        "ProjectName",
        String(200),
    )

    description: Mapped[str | None] = mapped_column(
        "Description",
        String(1000),
    )

    user = relationship(
        "User",
        back_populates="projects",
    )