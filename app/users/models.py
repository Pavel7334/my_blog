from sqlalchemy import Column, Integer, String

from app.database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False)
    is_admin = Column(bool, default=False)
