from fastapi import HTTPException, status

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.auth import RegisterRequest, LoginRequest
from app.security.hashing import hash_password, verify_password
from app.security.jwt import create_access_token


class AuthService:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def register(self, request: RegisterRequest):

        if self.repository.get_by_email(request.email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already exists",
            )

        if self.repository.get_by_username(request.username):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already exists",
            )

        try:

            user = User(
                username=request.username,
                email=request.email,
                password_hash=hash_password(request.password),
                first_name=request.first_name,
                last_name=request.last_name,
            )

            user = self.repository.create(user)

            self.repository.db.commit()

            return user

        except Exception:

            self.repository.db.rollback()
            raise

    def login(self, request: LoginRequest):

        user = self.repository.get_by_email(request.email)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )

        if not verify_password(
            request.password,
            user.password_hash,
        ):
            raise ValueError("Invalid email or password")

        token = create_access_token(
            {
                "sub": str(user.user_id),
                "email": user.email,
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer",
        }