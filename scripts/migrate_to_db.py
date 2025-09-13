from backend.models import Item, Topic, ItemTypeEnum
from backend.database import AsyncSessionFactory
import sys
from pathlib import Path
import asyncio
import orjson
from loguru import logger
from sqlalchemy import text

SRC_PATH = Path(__file__).resolve().parent.parent / "backend"
sys.path.append(str(SRC_PATH))


JSON_FILE = Path("data.json")


async def migrate_data():
    logger.info(f"Reading data from {JSON_FILE}...")
    try:
        with JSON_FILE.open('rb') as f:
            data = orjson.loads(f.read())
    except FileNotFoundError:
        logger.error(f"Source data file not found: {JSON_FILE}")
        return

    logger.info(f"Found {len(data)} records to migrate.")
    logger.info("Sorting data by title before insertion...")
    data.sort(key=lambda item: item.get('title', '').lower())

    async with AsyncSessionFactory() as session:
        async with session.begin():
            logger.warning("Resetting 'items' and 'topics' tables...")
            await session.execute(text("TRUNCATE TABLE items, topics RESTART IDENTITY CASCADE;"))

            logger.info("Inserting new records in alphabetical order...")
            for item_data in data:
                new_item = Item(
                    title=item_data.get('title'),
                    source=item_data.get('file_name'),
                    item_type=ItemTypeEnum.BOOK,
                    attributes={"format": "pdf"}
                )
                session.add(new_item)

        await session.commit()

    logger.success(f"Successfully migrated {len(data)} items to the database.")

if __name__ == "__main__":
    asyncio.run(migrate_data())
