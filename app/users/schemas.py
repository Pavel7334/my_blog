from pydantic import BaseModel


class SUser(BaseModel):
    username: str
    is_admin: bool
