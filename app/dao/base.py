from sqlalchemy import select, insert, delete, update

from app import posts
from app.database import async_session_maker
from app.posts.models import Post


class BaseDAO:
    model = None

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().one_or_none()

    @classmethod
    async def find_all(cls, limit: int = 25, page: int = 1, search_title=None, search_username=None):
        if page > 0:
            page -= 1
        offset = page * limit
        async with async_session_maker() as session:
            query = select(
                cls.model.__table__.columns,
            ).limit(limit).offset(offset)
            if search_title:
                query = query.where(cls.model.title.ilike(f'%{search_title}%'))
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def update(cls, id: int, **data):
        async with async_session_maker() as session:
            query = update(cls.model).filter_by(id=id).values(**data).returning(cls.model)
            result = await session.execute(query)
            await session.commit()
            return result.fetchone()[0]

    @classmethod
    async def delete(cls, **filter_by):
        async with async_session_maker() as session:
            query = delete(cls.model).filter_by(**filter_by)
            await session.execute(query)
            await session.commit()
