import uuid

from enum import Enum

from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseModel


class UserRole(str, Enum):
    ADMIN = "Admin"
    USER = "User"
    CREATOR = "Creator"


class User(BaseModel):
    __tablename__ = "Users"

    user_id: Mapped[int] = mapped_column(
        "UserId",
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

    username: Mapped[str] = mapped_column(
        "Username",
        String(50),
        unique=True,
        nullable=False,
        index=True,
    )

    email: Mapped[str] = mapped_column(
        "Email",
        String(255),
        unique=True,
        nullable=False,
        index=True,
    )

    password_hash: Mapped[str] = mapped_column(
        "PasswordHash",
        String(255),
        nullable=False,
    )

    first_name: Mapped[str] = mapped_column(
        "FirstName",
        String(100),
        nullable=False,
    )

    last_name: Mapped[str] = mapped_column(
        "LastName",
        String(100),
        nullable=False,
    )

    profile_image: Mapped[str | None] = mapped_column(
        "ProfileImage",
        String(500),
        nullable=True,
    )

    role: Mapped[str] = mapped_column(
        "Role",
        String(50),
        default=UserRole.USER.value,
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        "IsActive",
        Boolean,
        default=True,
        nullable=False,
    )

    projects = relationship(
        "Project",
        back_populates="user",
        cascade="all, delete-orphan",
    )