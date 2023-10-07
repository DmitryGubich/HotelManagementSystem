from app.users.auth import get_password_hash
from app.users.schemas import SchemaUserSignUp
from app.users.service import UserService
from fastapi import APIRouter, HTTPException

auth_router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)

router_users = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@auth_router.post("/sign-up")
async def sign_up(user_data: SchemaUserSignUp):
    existing_user = await UserService.find_one_or_none(email=user_data.email)

    if existing_user:
        raise HTTPException(
            status_code=409, detail="User with given email already exists"
        )

    if user_data.password != user_data.repeat_password:
        raise HTTPException(status_code=409, detail="Passwords must match")

    hashed_password = get_password_hash(user_data.password)
    new_user = await UserService.create(
        email=user_data.email, hashed_password=hashed_password
    )

    if not new_user:
        raise HTTPException(status_code=500)
