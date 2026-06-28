from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.base_model import BaseModel


class User(BaseModel):

    __tablename__ = "Users"

    UserId: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    FirstName: Mapped[str] = mapped_column(
        String(100)
    )

    LastName: Mapped[str] = mapped_column(
        String(100)
    )

    Email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )

    PasswordHash: Mapped[str] = mapped_column(
        String(255)
    )

    IsActive: Mapped[bool]

from sqlalchemy.orm import relationship

Projects = relationship(
    "Project",
    back_populates="user"
)

user = relationship(
    "User",
    back_populates="Projects"
)