import asyncio
from sqlalchemy import text

from backend.database import engine
from backend.models import Base

async def init_db():
    async with engine.begin() as conn:
        print("Resetting the public schema...")
        await conn.execute(text("DROP SCHEMA public CASCADE"))
        await conn.execute(text("CREATE SCHEMA public"))
        
        print("Creating all tables...")
        await conn.run_sync(Base.metadata.create_all)
        
        print("Tables created successfully.")

if __name__ == "__main__":
    print("Connecting to the database to create tables...")
    asyncio.run(init_db())