from app.base.repository import BaseRepository
from app.exceptions import EntityNotFoundException


class BaseService:
    repository: BaseRepository = None

    @classmethod
    async def find_by_id(cls, model_id):
        result = await cls.repository.find_by_id(model_id)
        if not result:
            raise EntityNotFoundException
        return result

    @classmethod
    async def filter(cls, **filter_by):
        return await cls.repository.filter(**filter_by)

    @classmethod
    async def find_all(cls, **filter_by):
        return await cls.repository.find_all(**filter_by)

    @classmethod
    async def delete(cls, model_id):
        result = await cls.repository.delete(model_id)
        if not result:
            raise EntityNotFoundException
        return result

    @classmethod
    async def update(cls, model_id, **data):
        return await cls.repository.update(model_id, **data)

    @classmethod
    async def create(cls, **data):
        return await cls.repository.create(**data)
