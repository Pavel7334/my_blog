from fastapi import APIRouter

from app.blogs.dao import BlogDAO
from app.blogs.schemas import SBlog, SBlogUpdate, SBlogList
from app.exceptions import BlogAlreadyExistException, BlogDoesNotExistException

router = APIRouter(
    prefix="/blog",
    tags=["Блог"],
)


@router.get("")
async def get_blogs(
        limit: int = 25,
        page: int = 1,
        search_title=None,
        search_username=None
) -> SBlogList:
    blogs = await BlogDAO.find_all(limit, page, search_title)
    return SBlogList(
        results=blogs,
        page=page,
        limit=limit,
        search_title=search_title
    )


@router.get('/{blog_id}')
async def get_blog_id(
    blog_id: int,
):
    existing_blog = await BlogDAO.find_one_or_none(id=blog_id)
    if not existing_blog:
        raise BlogDoesNotExistException
    return existing_blog


@router.post("")
async def add_blog(new_blog: SBlog):
    existing_blog = await BlogDAO.find_one_or_none(title=new_blog.title)
    if existing_blog:
        raise BlogAlreadyExistException
    await BlogDAO.add(
        title=new_blog.title,
        description=new_blog.description,
        owner_id=new_blog.owner_id,
    )


@router.patch("/{blog_id}")
async def update_blog(blog_id: int, new_blog: SBlogUpdate):
    existing_blog = await BlogDAO.find_one_or_none(id=blog_id)
    if not existing_blog:
        raise BlogDoesNotExistException
    return await BlogDAO.update(
        id=blog_id,
        title=new_blog.title,
        description=new_blog.description,
        owner_id=new_blog.owner_id,
    )


@router.delete("/{blog_id}")
async def remove_blog(
    blog_id: int,
):
    await BlogDAO.delete(id=blog_id)

