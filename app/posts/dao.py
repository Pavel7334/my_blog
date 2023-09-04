from app.dao.base import BaseDAO
from app.posts.models import Posts


class PostsDAO(BaseDAO):
    model = Posts
