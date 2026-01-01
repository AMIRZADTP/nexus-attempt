import asyncio
import json
from pathlib import Path

from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine

from nexus.infrastructure.persistence.models import Base, Item, ItemTypeEnum
from nexus.infrastructure.persistence.database import DATABASE_URL

# data.json is at project root. init_db.py is in src/nexus/infrastructure
# So parent (infra) -> parent (nexus) -> parent (src) -> parent (root)
JSON_INPUT_FILE = Path(__file__).resolve().parent.parent.parent.parent / "data.json"


async def main() -> None:
    print("Initializing database...")
    engine = create_async_engine(DATABASE_URL)

    async with engine.begin() as conn:
        print("Creating tables if they do not exist...")
        await conn.run_sync(Base.metadata.create_all)

    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT COUNT(1) FROM items"))
        item_count = result.scalar_one()

        if item_count == 0:
            print("Items table is empty. Migrating data from JSON...")
            with open(JSON_INPUT_FILE, encoding="utf-8") as f:
                data = json.load(f)

            items_to_add = [
                Item(
                    title=entry.get("title"),
                    source=entry.get("file_name"),
                    item_type=ItemTypeEnum.BOOK,
                    attributes={"format": "pdf"},
                )
                for entry in data
            ]

            print(f"{len(items_to_add)} items migrated successfully.")

            # Use AsyncSession for ORM operations
            from nexus.infrastructure.persistence.database import SessionLocal
            async with SessionLocal() as session:
                session.add_all(items_to_add)
                await session.commit()
        else:
            print("Database already contains data. Skipping migration.")

    await engine.dispose()
    print("Database initialization complete.")


if __name__ == "__main__":
    asyncio.run(main())
