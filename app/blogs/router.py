from fastapi import APIRouter, Depends
from sqlalchemy import insert

from app.blogs.dao import BlogDAO
from app.blogs.models import Blog
from app.blogs.schemas import SBlog
from app.exceptions import BlogAlreadyExistException

router = APIRouter(
    prefix="/blog",
    tags=["Блог"],
)


@router.post("/")
async def add_blogs(new_blog: SBlog):
    existing_blog = await BlogDAO.find_one_or_none(title=new_blog.title)
    if existing_blog:
        raise BlogAlreadyExistException
    await BlogDAO.add(
        title=new_blog.title,
        description=new_blog.description,
        owner_id=new_blog.owner_id,
    )