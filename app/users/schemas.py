from pydantic import BaseModel, EmailStr


class SUserAuth(BaseModel):
    email: EmailStr
    password: str
    username: str


class SUser(BaseModel):
    username: str
    is_admin: bool
