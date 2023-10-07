from pydantic import BaseModel, EmailStr


class SchemaUserSignUp(BaseModel):
    email: EmailStr
    password: str
    repeat_password: str
