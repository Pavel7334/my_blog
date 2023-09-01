from datetime import datetime

from sqlalchemy import Integer, Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Blogs(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    owner_id = Column(ForeignKey("users.id"))

    authors_id = relationship("Users", back_populates="blog")

