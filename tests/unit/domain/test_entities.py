from nexus.domain.entities import Item, ItemType

def test_item_creation():
    item = Item(title="Test Book", item_type=ItemType.BOOK)
    assert item.title == "Test Book"
    assert item.uuid is not None  # Should auto-generate
    assert item.is_book() is True
    assert item.topics == []

def test_item_is_not_book():
    item = Item(title="Bookmark", item_type=ItemType.BOOKMARK)
    assert item.is_book() is False
