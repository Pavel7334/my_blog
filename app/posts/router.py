from datetime import datetime

from fastapi import APIRouter, Depends

from app.database import async_session_maker
from app.exceptions import PostDoesNotExistException
from app.posts.dao import PostDAO
from app.posts.models import Post
from app.posts.schemas import SPost, SPostUpdate, SPostList, SPostBlogFilter

router = APIRouter(
    prefix="/post",
    tags=["Пост"],
)


@router.get("")
async def get_posts(
        filters: SPostBlogFilter = Depends()
        ) -> SPostList:
    posts = await PostDAO.find_all(filters)
    return SPostList(
        results=posts,
        page=SPostBlogFilter.page,
        limit=SPostBlogFilter.limit,
        search_title=SPostBlogFilter.search_title,
        search_username=SPostBlogFilter.search_username,
        filter_date_from=SPostBlogFilter.filter_date_from,
        filter_dates_to=SPostBlogFilter.filter_dates_to
    )


@router.get('/{post_id}')
async def get_post_id(
    post_id: int,
):
    existing_post = await PostDAO.find_one_or_none(id=post_id)
    if not existing_post:
        raise PostDoesNotExistException
    new_counter = existing_post.views
    new_counter += 1
    return await PostDAO.update(id=post_id, views=new_counter)


@router.post("")
async def add_post(new_post: SPost):
    await PostDAO.add(
        blog_id=new_post.blog_id,
        authors_id=new_post.authors_id,
        title=new_post.title,
        body=new_post.body,
        is_published=new_post.is_published
    )


@router.patch("/{post_id}")
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


@router.delete("/{post_id}")
async def remove_post(
    post_id: int,
):
    await PostDAO.delete(id=post_id)
