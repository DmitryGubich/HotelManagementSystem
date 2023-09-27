from app.base.repository import BaseRepository
from fastapi import HTTPException


class BaseService:
    repository: BaseRepository = None

    @classmethod
    async def find_by_id(cls, model_id):
        result = await cls.repository.find_by_id(model_id)
        if not result:
            raise HTTPException(status_code=404, detail="Item does not exist.")
        return result

    @classmethod
    async def find_all(cls, **filter_by):
        result = await cls.repository.find_all(**filter_by)
        return result
