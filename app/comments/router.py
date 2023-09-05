from fastapi import APIRouter

from app.comments.dao import CommentDAO
from app.comments.schemas import SComment
router = APIRouter(
    prefix="/comment",
    tags=["Комментарий"],
)


@router.post("/")
async def add_comment(new_comment: SComment):
    await CommentDAO.add(
        posts_id=new_comment.posts_id,
        authors_id=new_comment.authors_id,
        body=new_comment.body
    )
