from fastapi import APIRouter

router = APIRouter(
    prefix="/video",
    tags=["Video"],
)

@router.post(
    "/demo",
)
def generate_video():
    return {"message": f"demo"}