from datetime import datetime

from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base import Base


class BaseModel(Base):
    __abstract__ = True

    CreatedAt: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    UpdatedAt: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    CreatedBy: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    UpdatedBy: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    IsDeleted: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False
    )