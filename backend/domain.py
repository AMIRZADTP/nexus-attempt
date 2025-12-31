import uuid

from pydantic import BaseModel, ConfigDict, field_validator
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .cache import CACHE_KEYS, get_or_set
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

    @field_validator("created_at", mode="before")
    def format_date(cls, v):
        if v:
            return v.strftime("%Y-%m-%d %H:%M")
        return "N/A"


async def fetch_all_items(
    db_session: AsyncSession, skip: int = 0, limit: int = 100
) -> list[ItemSummary]:
    """
    Fetch all items with pagination.

    Results are cached for 5 minutes to avoid repeated DB queries.
    Cache key includes skip and limit for proper pagination caching.
    """
    cache_key = CACHE_KEYS["items_list"].format(skip=skip, limit=limit)

    async def _fetch_from_db():
        query = select(ItemModel).order_by(ItemModel.title).offset(skip).limit(limit)
        result = await db_session.execute(query)
        items_from_db = result.scalars().all()
        # Convert to dicts for caching (Pydantic models aren't directly cacheable)
        return [{"uuid": str(item.uuid), "title": item.title} for item in items_from_db]

    cached_items = await get_or_set(cache_key, _fetch_from_db)

    # Convert cached dicts back to Pydantic models
    return [
        ItemSummary(uuid=item["uuid"], title=item["title"]) for item in cached_items
    ]


async def fetch_item_by_uuid(
    db_session: AsyncSession, item_uuid: uuid.UUID
) -> ItemModel | None:
    """
    Fetch a single item by UUID.

    Note: We don't cache this because the ItemModel contains
    SQLAlchemy relationships that don't serialize well.
    For single-item lookups, the DB hit is acceptable.

    TODO: Cache the serialized ItemDetail instead if needed.
    """
    query = select(ItemModel).where(ItemModel.uuid == item_uuid)
    result = await db_session.execute(query)
    return result.scalar_one_or_none()
