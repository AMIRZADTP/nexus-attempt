from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID
from nexus.domain.entities import Item

class ItemRepository(ABC):
    """
    Interface for Item data access.
    The domain layer defines this interface; Infrastructure implements it.
    """

    @abstractmethod
    async def add(self, item: Item) -> Item:
        """Add a new item to the repository."""
        pass

    @abstractmethod
    async def get_by_uuid(self, uuid: UUID) -> Optional[Item]:
        """Retrieve an item by its UUID."""
        pass

    @abstractmethod
    async def list_items(self, skip: int = 0, limit: int = 100) -> List[Item]:
        """List items with pagination."""
        pass
