from typing import Generic, TypeVar

from pydantic import BaseModel

from app.db.base_class import Base
from app.repositories.base import BaseRepository

# Нужно ОБЯЗАТЕЛЬНО добавить bound, как и в репозитории
ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BaseService(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, repository: BaseRepository[ModelType, CreateSchemaType, UpdateSchemaType]):
        self.repository = repository
