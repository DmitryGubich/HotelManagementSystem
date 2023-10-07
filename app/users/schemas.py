from pydantic import BaseModel, EmailStr


class SchemaUserSignUp(BaseModel):
    email: EmailStr
    username: str
    password: str
    repeat_password: str


class SchemaUseLogIn(BaseModel):
    email: EmailStr
    password: str


class SchemaUser(BaseModel):
    id: int
    email: EmailStr
    username: str
