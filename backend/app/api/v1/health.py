from sqlalchemy import text
from sqlalchemy.orm import Session

from fastapi import APIRouter
from fastapi import Depends

from app.dependencies.database import get_db
from app.core.config import settings

router = APIRouter(
    prefix="/api/v1",
    tags=["Health"],
)


@router.get("/health")
def health(db: Session = Depends(get_db)):
    """
    Health check endpoint.

    Checks:
    - FastAPI is running
    - SQL Server connection
    """

    try:
        db.execute(text("SELECT 1"))

        database_status = "connected"

    except Exception as ex:

        database_status = "disconnected"

        return {
            "status": "unhealthy",
            "database": database_status,
            "error": str(ex),
            "version": settings.APP_VERSION
        }

    return {
        "status": "healthy",
        "database": database_status,
        "version": settings.APP_VERSION
    }