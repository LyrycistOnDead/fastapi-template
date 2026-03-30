from typing import Annotated

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies.db import get_db

router = APIRouter()


class HealthCheckResponse(BaseModel):
    status: str
    database: str
    result: int


db_dep = Annotated[AsyncSession, Depends(get_db)]


@router.get("/db-check", response_model=HealthCheckResponse)
async def check_db_connection(db: db_dep):
    query = await db.execute(text("SELECT 1"))
    scalar_result = int(query.scalar() or 0)

    return HealthCheckResponse(status="connected", database="postgresql", result=scalar_result)
