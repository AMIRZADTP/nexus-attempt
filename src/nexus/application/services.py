from typing import List, Optional
from uuid import UUID

from nexus.domain.entities import Item
from nexus.domain.repositories import ItemRepository
from nexus.infrastructure.cache.memory import get_or_set, CACHE_KEYS

class ItemService:
    def __init__(self, repository: ItemRepository):
        self.repository = repository

    async def list_items(self, skip: int = 0, limit: int = 100) -> List[Item]:
        # Cache logic remains here (Application concern) or decorator?
        # For now, let's keep it explicit as per old services.py
        
        cache_key = CACHE_KEYS["items_list"].format(skip=skip, limit=limit)
        
        async def _fetch():
            # Returns Entities, not dicts
            return await self.repository.list_items(skip=skip, limit=limit)
            
        # We need to adapt the cache behavior because cache might store dicts?
        # If get_or_set pickles, entities are fine. 
        # But if it expects dicts, we might need serialization.
        # Let's assume in-memory cache handles objects.
        
        return await get_or_set(cache_key, _fetch)

    async def get_item(self, item_uuid: UUID) -> Optional[Item]:
        return await self.repository.get_by_uuid(item_uuid)
