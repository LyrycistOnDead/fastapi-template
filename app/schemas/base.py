from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    """
    Базовая схема с общими настройками.
    """

    model_config = ConfigDict(from_attributes=True)


class BaseIDSchema(BaseSchema):
    """
    Базовая схема для объектов, у которых точно есть ID.
    """

    id: int
