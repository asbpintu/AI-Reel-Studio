from fastapi import APIRouter
from fastapi import Depends
from fastapi import status

from app.dependencies.services import get_auth_service
from app.schemas.auth import RegisterRequest
from app.schemas.auth import UserResponse
from app.services.auth_service import AuthService

from app.schemas.auth import LoginRequest
from app.schemas.auth import TokenResponse

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user",
    description="Creates a new user account.",
)
def register(
    request: RegisterRequest,
    service: AuthService = Depends(get_auth_service),
):
    return service.register(request)


@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    request: LoginRequest,
    service: AuthService = Depends(get_auth_service),
):
    return service.login(request)