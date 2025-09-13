import configparser
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from pathlib import Path

# --- 1. Define the project root directory dynamically ---
# Path(__file__) is the path to the current file (database.py)
# .resolve() makes the path absolute
# .parent.parent gets the root directory ("nexus-attempt/")
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# --- 2. Construct the absolute path to the config file ---
CONFIG_FILE_PATH = PROJECT_ROOT / 'config.ini'

config = configparser.ConfigParser()
config.read(CONFIG_FILE_PATH)

db_config = config['Database']
DATABASE_URL = (
    f"postgresql+asyncpg://{db_config['user']}:{db_config['password']}"
    f"@{db_config['host']}:{db_config['port']}/{db_config['dbname']}"
)

engine = create_async_engine(DATABASE_URL, echo=True)

AsyncSessionFactory = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession
)
