from app.dao.base import BaseDAO
from app.blogs.models import Blog


class BlogDAO(BaseDAO):
    model = Blog