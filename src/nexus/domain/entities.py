from datetime import datetime
from enum import StrEnum
from typing import Dict, Any, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, ConfigDict, Field

class ItemType(StrEnum):
    BOOK = "book"
    BOOKMARK = "bookmark"
    NOTE = "note"
    UNCATEGORIZED = "uncategorized"

class DomainEntity(BaseModel):
    """
    Base class for all domain entities.
    Enforces immutability and strict config.
    """
    model_config = ConfigDict(frozen=True, from_attributes=True)

class Topic(DomainEntity):
    id: Optional[int] = None
    name: str

class Item(DomainEntity):
    id: Optional[int] = None
    uuid: UUID = Field(default_factory=uuid4)
    title: str
    source: Optional[str] = None
    item_type: ItemType = ItemType.UNCATEGORIZED
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.now)
    topics: list[Topic] = Field(default_factory=list)

    def is_book(self) -> bool:
        return self.item_type == ItemType.BOOK
