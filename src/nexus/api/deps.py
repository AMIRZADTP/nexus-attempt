from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from nexus.infrastructure.database import SessionLocal


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session
