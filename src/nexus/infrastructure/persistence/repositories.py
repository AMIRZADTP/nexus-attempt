from typing import List, Optional, Any
from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from nexus.domain.entities import Item as ItemEntity
from nexus.domain.repositories import ItemRepository
from nexus.infrastructure.persistence.models import Item as ItemModel

class SqlAlchemyItemRepository(ItemRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, item: ItemEntity) -> ItemEntity:
        # Map Entity -> ORM
        item_model = ItemModel(
            uuid=item.uuid,
            title=item.title,
            source=item.source,
            item_type=item.item_type, # Enum should map automatically if compatible
            attributes=item.attributes,
            created_at=item.created_at
            # Topics not handled in add yet, assuming empty list or verified later
        )
        self.session.add(item_model)
        # We don't commit here; Unit of Work should handle commit. 
        # But for simplicity in this refactor, let's assume service commits or we auto-flush.
        # Ideally, Repository just adds to session.
        await self.session.flush() # Populate IDs
        return item # In a real mapper, we might map back from model to get DB-generated IDs

    async def get_by_uuid(self, uuid: UUID) -> Optional[ItemEntity]:
        query = select(ItemModel).options(selectinload(ItemModel.topics)).where(ItemModel.uuid == uuid)
        result = await self.session.execute(query)
        item_model = result.scalar_one_or_none()
        
        if not item_model:
            return None
            
        # Map ORM -> Entity
        return ItemEntity.model_validate(item_model)

    async def list_items(self, skip: int = 0, limit: int = 100) -> List[ItemEntity]:
        query = select(ItemModel).options(selectinload(ItemModel.topics)).offset(skip).limit(limit)
        result = await self.session.execute(query)
        item_models = result.scalars().all()
        
        return [ItemEntity.model_validate(m) for m in item_models]
