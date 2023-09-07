from fastapi import APIRouter

from app.exceptions import PostDoesNotExistException
from app.posts.dao import PostDAO
from app.posts.schemas import SPost, SPostUpdate, SPostList

router = APIRouter(
    prefix="/post",
    tags=["Пост"],
)


@router.get("")
async def get_posts(limit: int = 25, page: int = 1) -> SPostList:
    posts = await PostDAO.find_all(limit, page)
    return SPostList(results=posts, page=page, limit=limit)


@router.get('/{post_id}')
async def get_post_id(
    post_id: int,
):
    existing_post = await PostDAO.find_one_or_none(id=post_id)
    if not existing_post:
        raise PostDoesNotExistException
    return existing_post


@router.post("/")
async def add_post(new_post: SPost):
    await PostDAO.add(
        blog_id=new_post.blog_id,
        authors_id=new_post.authors_id,
        title=new_post.title,
        body=new_post.body,
        is_published=new_post.is_published
    )


@router.put("/{post_id}")
async def update_post(post_id: int, new_posts: SPostUpdate):
    existing_post = await PostDAO.find_one_or_none(id=post_id)
    if not existing_post:
        raise PostDoesNotExistException
    return await PostDAO.update(
        id=post_id,
        blog_id=new_posts.blog_id,
        authors_id=new_posts.authors_id,
        title=new_posts.title,
        body=new_posts.body,
    )
