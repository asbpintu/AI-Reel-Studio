from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings
from app.api.v1.projects import router as project_router
from app.api.v1.auth import router as auth_router
from app.api.v1.users import router as user_router

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