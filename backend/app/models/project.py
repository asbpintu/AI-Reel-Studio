from sqlalchemy import ForeignKey
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base_model import BaseModel


class Project(BaseModel):

    __tablename__ = "Projects"

    ProjectId: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    UserId: Mapped[int] = mapped_column(
        ForeignKey("Users.UserId")
    )

    ProjectName: Mapped[str] = mapped_column(
        String(200)
    )

    Description: Mapped[str | None] = mapped_column(
        String(1000)
    )

    user = relationship("User", back_populates="projects")