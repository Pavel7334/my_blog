from pydantic import BaseModel


class SPost(BaseModel):
    blog_id: int
    authors_id: int
    title: str
    bode: str
    is_published: bool
    likes = int
    views = int
