from pydantic import BaseModel


class SComment(BaseModel):
    posts_id: int
    authors_id: int
    body: str
