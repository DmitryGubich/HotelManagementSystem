from app.database import Base, async_session_maker
from sqlalchemy import insert, select, update


class BaseRepository:
    model: Base = None

    @classmethod
    async def find_by_id(cls, model_id):
        query = select(cls.model.__table__.columns).filter_by(id=model_id)
        async with async_session_maker() as session:
            result = await session.execute(query)
            return result.mappings().one_or_none()

    @classmethod
    async def filter(cls, **filter_by):
        query = select(cls.model.__table__.columns).filter_by(**filter_by)
        async with async_session_maker() as session:
            result = await session.execute(query)
            return result.mappings().one_or_none()

    @classmethod
    async def find_all(cls, **filter_by):
        query = select(cls.model.__table__.columns).filter_by(**filter_by)
        async with async_session_maker() as session:
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def create(cls, **data):
        query = insert(cls.model).values(**data).returning(cls.model)
        async with async_session_maker() as session:
            result = await session.execute(query)
            await session.commit()
            return result.mappings().first()

    @classmethod
    async def update(cls, model_id, **data):
        query = (
            update(cls.model)
            .where(cls.model.c.id == model_id)
            .values(**data)
            .returning(cls.model)
        )
        async with async_session_maker() as session:
            result = await session.execute(query)
            return result.mappings().first()

    @classmethod
    async def delete(cls, model_id):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(id=model_id)
            if not query:
                return False
            await session.delete(query)
            await session.commit()
            return True
