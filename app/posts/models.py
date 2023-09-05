from datetime import datetime

from sqlalchemy import Integer, Column, String, DateTime, ForeignKey, Boolean

from app.database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    blog_id = Column(ForeignKey("blogs.id"))
    authors_id = Column(ForeignKey("users.id"))
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)
    is_published = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    likes = Column(Integer, default=0)
    views = Column(Integer, default=0)
