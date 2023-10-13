from typing import Annotated

from app.users.dependencies import get_current_user
from app.users.models import Users
from app.users.schemas import SchemaUser, SchemaUserSignUp, Token
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
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    return await UserService.login(form_data=form_data)


@auth_router.get("/me")
async def me(user: Users = Depends(get_current_user)) -> SchemaUser:
    return SchemaUser(id=user.id, email=user.email, username=user.username)
