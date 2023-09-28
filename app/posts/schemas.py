from datetime import datetime
from typing import Optional

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


class SPostBlogFilter(BaseModel):
    limit: int = 25
    page: int = 1
    search_title: Optional[str] = None
    search_username: Optional[str] = None
    filter_date_from: Optional[datetime] = None
    filter_dates_to: Optional[datetime] = None

