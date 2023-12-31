from sqlalchemy import select, insert, delete, update, desc

from app.database import async_session_maker
from app.posts.models import Post
from app.users.models import User


class BaseDAO:
    model = None

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().one_or_none()

    @classmethod
    def filter_query(cls, query, filters):
        if filters.search_title:
            query = query.where(cls.model.title.ilike(f'%{filters.search_title}%'))
        if filters.search_username:
            query = query.join(User).where(User.username.ilike(f'%{filters.search_username}%'))
        if filters.filter_date_from:
            query = query.where(cls.model.created_at > filters.filter_date_from)
        if filters.filter_date_to:
            query = query.where(cls.model.created_at < filters.filter_date_to)
        return query

    @classmethod
    def sorting_query(cls, query, filters):
        sort_values = {
            'title': cls.model.title,
            'created_at': cls.model.created_at,
            'likes': Post.likes,
        }
        if filters.sort_order == 'asc':
            query = query.order_by(sort_values.get(filters.sort_by))
        elif filters.sort_order == 'desc':
            query = query.order_by(desc(sort_values.get(filters.sort_by)))
        return query

    @classmethod
    async def find_all(cls, filters):
        if filters.page > 0:
            filters.page -= 1
        offset = filters.page * filters.limit
        async with async_session_maker() as session:
            query = select(
                cls.model.__table__.columns,
            ).limit(filters.limit).offset(offset)
            query = cls.filter_query(query, filters)
            query = cls.sorting_query(query, filters)
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
