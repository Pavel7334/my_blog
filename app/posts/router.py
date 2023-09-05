from fastapi import APIRouter

from app.posts.dao import PostDAO
from app.posts.schemas import SPost

router = APIRouter(
    prefix="/post",
    tags=["Пост"],
)


@router.post("/")
async def add_post(new_post: SPost):
    await PostDAO.add(
        blog_id=new_post.blog_id,
        authors_id=new_post.authors_id,
        title=new_post.title,
        body=new_post.body,
        is_published=new_post.is_published
    )
