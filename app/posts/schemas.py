from datetime import datetime

from pydantic import BaseModel


class SPosts(BaseModel):
    blog_id: int
    authors_id: int
    title: str
    bode: str
    is_published: bool
    likes = int
    views = int
