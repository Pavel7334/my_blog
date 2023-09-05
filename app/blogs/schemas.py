from pydantic import BaseModel


class SBlog(BaseModel):
    title: str
    description: str
    owner_id: int

    class Config:
        from_attributes = True