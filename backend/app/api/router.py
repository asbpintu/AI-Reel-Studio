from fastapi import APIRouter
from app.api.v1 import auth, health, users, projects, scripts, scenes, images, audios

api_router = APIRouter()

api_router.include_router(health.router)
api_router.include_router(auth.router)
api_router.include_router(users.router)
api_router.include_router(projects.router)
api_router.include_router(scripts.router)
api_router.include_router(scenes.router)
api_router.include_router(images.router)
api_router.include_router(audios.router)