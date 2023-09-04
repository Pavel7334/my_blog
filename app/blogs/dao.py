from app.dao.base import BaseDAO
from app.blogs.models import Blogs


class BlogsDAO(BaseDAO):
    model = Blogs