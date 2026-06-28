from typing import Generic
from typing import TypeVar

from sqlalchemy.orm import Session

T = TypeVar("T")


class BaseRepository(Generic[T]):

    def __init__(self, db: Session):

        self.db = db