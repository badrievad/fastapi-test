from .schemas import User
from fastapi import APIRouter


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post("/create/")
def create_user(user: User):
    return {"success": True, "user": user.name}


@router.get("/")
def get_users():
    return [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]
