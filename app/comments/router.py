from fastapi import APIRouter, Depends

from app.comments.dao import CommentDAO
from app.comments.schemas import SComment, SCommentUpdate
from app.exceptions import CommentDoesNotExistException
from app.users.authorization import JWTBearer

router = APIRouter(
    prefix="/comment",
    tags=["Комментарий"],
)


@router.post("/comment", dependencies=[Depends(JWTBearer())])
async def add_comment(new_comment: SComment):
    await CommentDAO.add(
        posts_id=new_comment.posts_id,
        authors_id=new_comment.authors_id,
        body=new_comment.body
    )


@router.patch("/{comment_id}")
async def update_comment(comment_id: int, new_comment: SCommentUpdate):
    existing_comment = await CommentDAO.find_one_or_none(id=comment_id)
    if not existing_comment:
        raise CommentDoesNotExistException
    return await CommentDAO.update(
        id=comment_id,
        posts_id=new_comment.posts_id,
        authors_id=new_comment.authors_id,
        body=new_comment.body,
    )


@router.delete("/{comment_id}")
async def remove_post(
        comment_id: int,
):
    await CommentDAO.delete(id=comment_id)
