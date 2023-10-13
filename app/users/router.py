from typing import Annotated

from app.users.schemas import SchemaUser, SchemaUserSignUp
from app.users.service import UserService
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

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
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    return await UserService.login(form_data=form_data)


# @auth_router.post("/me")
# async def me(user: Users = Depends(get_current_user)) -> Users:
#     return user
