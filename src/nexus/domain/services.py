import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from nexus.infrastructure.cache import CACHE_KEYS, get_or_set
from nexus.domain.models import Item as ItemModel
from nexus.domain.schemas import ItemSummary


async def fetch_all_items(
    db_session: AsyncSession,
    skip: int = 0,
    limit: int = 100
) -> list[ItemSummary]:
    """
    Fetch all items with pagination.
    
    Results are cached for 5 minutes to avoid repeated DB queries.
    """
    cache_key = CACHE_KEYS["items_list"].format(skip=skip, limit=limit)
    
    async def _fetch_from_db() -> list[dict[str, str]]:
        query = select(ItemModel).order_by(
            ItemModel.title).offset(skip).limit(limit)
        result = await db_session.execute(query)
        items_from_db = result.scalars().all()
        return [
            {"uuid": str(item.uuid), "title": item.title}
            for item in items_from_db
        ]
    
    cached_items = await get_or_set(cache_key, _fetch_from_db)
    
    return [ItemSummary(uuid=item["uuid"], title=item["title"]) for item in cached_items]


async def fetch_item_by_uuid(
    db_session: AsyncSession,
    item_uuid: uuid.UUID
) -> ItemModel | None:
    """
    Fetch a single item by UUID.
    """
    query = select(ItemModel).where(ItemModel.uuid == item_uuid)
    result = await db_session.execute(query)
    return result.scalar_one_or_none()
