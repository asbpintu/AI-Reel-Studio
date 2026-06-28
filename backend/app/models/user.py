import uuid

from sqlalchemy import Boolean
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base_model import BaseModel
from enum import Enum


class UserRole(str, Enum):
    ADMIN = "Admin"
    USER = "User"
    CREATOR = "Creator"


class User(BaseModel):
    __tablename__ = "Users"

    UserId: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    PublicId: Mapped[str] = mapped_column(
        String(36),
        default=lambda: str(uuid.uuid4()),
        unique=True,
        nullable=False,
        index=True
    )

    Username: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
        index=True
    )

    Email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True
    )

    PasswordHash: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    FirstName: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    LastName: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    ProfileImage: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )

    Role: Mapped[str] = mapped_column(
        String(50),
        default="User",
        nullable=False
    )

    IsActive: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

    Projects = relationship(
        "Project",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    Role: Mapped[str] = mapped_column(
    String(50),
    default=UserRole.USER.value,
    nullable=False
)


from sqlalchemy.orm import relationship

Projects = relationship(
    "Project",
    back_populates="user"
)

user = relationship(
    "User",
    back_populates="Projects"
)