from fastapi import APIRouter, Depends
from sqlalchemy import insert

from app.blogs.dao import BlogsDAO
from app.blogs.models import Blogs
from app.blogs.schemas import SBlogs
from app.exceptions import BlogsAlreadyExistException

router = APIRouter(
    prefix="/blogs",
    tags=["Блог"],
)


@router.post("/")
async def add_blogs(new_blogs: SBlogs):
    existing_blog = await BlogsDAO.find_one_or_none(title=new_blogs.title)
    if existing_blog:
        raise BlogsAlreadyExistException
    await BlogsDAO.add(
        title=new_blogs.title,
        description=new_blogs.description,
        owner_id=new_blogs.owner_id,
    )
