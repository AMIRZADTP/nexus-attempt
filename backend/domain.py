import uuid

from pydantic import BaseModel, ConfigDict, field_validator
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Item as ItemModel


class ItemSummary(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    uuid: uuid.UUID
    title: str


class ItemDetail(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    uuid: uuid.UUID
    title: str
    source: str | None = None
    item_type: str
    attributes: dict | None = None
    created_at: str

    @field_validator('created_at', mode='before')
    def format_date(cls, v):
        if v:
            return v.strftime('%Y-%m-%d %H:%M')
        return "N/A"


async def fetch_all_items(db_session: AsyncSession, skip: int = 0, limit: int = 100) -> list[ItemSummary]:
    query = select(ItemModel).order_by(
        ItemModel.title).offset(skip).limit(limit)
    result = await db_session.execute(query)
    items_from_db = result.scalars().all()
    return [ItemSummary.model_validate(item) for item in items_from_db]


async def fetch_item_by_uuid(db_session: AsyncSession, item_uuid: uuid.UUID) -> ItemModel | None:
    query = select(ItemModel).where(ItemModel.uuid == item_uuid)
    result = await db_session.execute(query)
    return result.scalar_one_or_none()
