from pydantic import BaseModel


class SPost(BaseModel):
    blog_id: int
    authors_id: int
    title: str
    body: str
    is_published: bool


class SPostUpdate(SPost):
    pass


class SPostList(BaseModel):
    results: list[SPost]
    limit: int
    page: int

