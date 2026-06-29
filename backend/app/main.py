from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="AI Reel Studio REST API",
    contact={
        "name": "Project Data"
    },
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def root():

    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running"
    }