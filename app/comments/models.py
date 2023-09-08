from datetime import datetime

from sqlalchemy import Integer, Column, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.database import Base


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    posts_id = Column(ForeignKey("posts.id", ondelete="CASCADE"))
    authors_id = Column(ForeignKey("users.id"))
    body = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
