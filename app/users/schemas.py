from pydantic import BaseModel, EmailStr


class SchemaUserSignUp(BaseModel):
    email: EmailStr
    username: str
    password: str
    repeat_password: str


class SchemaUseLogIn(BaseModel):
    username: str
    password: str


class SchemaUser(BaseModel):
    id: int
    email: EmailStr
    username: str


class Token(BaseModel):
    access_token: str
