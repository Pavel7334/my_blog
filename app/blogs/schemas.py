from pydantic import BaseModel


class SBlog(BaseModel):
    title: str
    description: str
    owner_id: int

    class Config:
        from_attributes = True


class SBlogUpdate(SBlog):
    pass


class SBlogList(BaseModel):
    results: list[SBlog]
    limit: int
    page: int
