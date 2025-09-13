import uuid
from typing import List, Optional
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel, field_validator

from .models import Item as ItemModel


class ItemSummary(BaseModel):
    uuid: uuid.UUID
    display_index: int
    title: str


class ItemDetail(BaseModel):
    id: int
    uuid: uuid.UUID
    title: str
    source: Optional[str] = None
    item_type: str
    attributes: Optional[dict] = None
    created_at: str

    @field_validator('created_at', mode='before')
    def format_date(cls, v):
        if v:
            return v.strftime('%Y-%m-%d %H:%M')
        return "N/A"

    class Config:
        from_attributes = True


async def fetch_all_items(db_session: AsyncSession) -> List[ItemSummary]:
    row_number_column = func.row_number().over(
        order_by=ItemModel.title).label("display_index")
    query = select(
        ItemModel.uuid,
        ItemModel.title,
        row_number_column
    ).order_by(ItemModel.title)

    result = await db_session.execute(query)

    items_from_db = result.all()

    items_as_response = [
        ItemSummary(
            uuid=item.uuid,
            display_index=item.display_index,
            title=item.title
        )
        for item in items_from_db
    ]
    return items_as_response


async def fetch_item_by_uuid(db_session: AsyncSession, item_uuid: uuid.UUID) -> Optional[ItemModel]:
    query = select(ItemModel).where(ItemModel.uuid == item_uuid)
    result = await db_session.execute(query)
    return result.scalar_one_or_none()
