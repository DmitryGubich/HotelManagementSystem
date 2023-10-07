from app.users.schemas import SchemaUseLogIn, SchemaUser, SchemaUserSignUp
from app.users.service import UserService
from fastapi import APIRouter

auth_router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)

users_router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@auth_router.post("/sign-up")
async def sign_up(user_data: SchemaUserSignUp) -> SchemaUser:
    return await UserService.sign_up(user_data=user_data)


@auth_router.post("/login")
async def login(user_data: SchemaUseLogIn) -> str:
    return await UserService.login(user_data=user_data)
