from datetime import datetime

from sqlalchemy import Boolean
from sqlalchemy import DateTime
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

    IsDeleted: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )