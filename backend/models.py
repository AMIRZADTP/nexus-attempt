import uuid
from sqlalchemy import (
    Column, Integer, String, Table, ForeignKey, DateTime, JSON, UUID, Enum
)
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func
import enum


class ItemTypeEnum(enum.Enum):
    BOOK = "book"
    BOOKMARK = "bookmark"
    NOTE = "note"
    UNCATEGORIZED = "uncategorized"


Base = declarative_base()

item_topic_association = Table(
    'item_topics',
    Base.metadata,
    Column('item_id', Integer, ForeignKey('items.id'), primary_key=True),
    Column('topic_id', Integer, ForeignKey('topics.id'), primary_key=True)
)


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4,
                  unique=True, nullable=False)
    title = Column(String, nullable=False)
    source = Column(String)
    item_type = Column(Enum(ItemTypeEnum),
                       default=ItemTypeEnum.UNCATEGORIZED, nullable=False)
    attributes = Column(JSON)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    topics = relationship(
        "Topic", secondary=item_topic_association, back_populates="items")


class Topic(Base):
    __tablename__ = 'topics'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    items = relationship(
        "Item", secondary=item_topic_association, back_populates="topics")
