from sqlalchemy import Column, Integer, String, Boolean, text
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    email = Column(String, server_default=text("'default@email.com'"), nullable=False)
    hashed_password = Column(String, server_default=text('123'), nullable=False)

    def __str__(self):
        return f"Пользователь {self.email}"

    # blogs = relationship("Blog", back_populates="user")

