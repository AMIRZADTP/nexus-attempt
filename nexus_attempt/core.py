import orjson
from pathlib import Path
from typing import List, Optional
from pydantic import BaseModel, ValidationError
from loguru import logger

# --- Data Structures ---


class Book(BaseModel):
    """
    Represents a single book entity using a Pydantic model.
    """
    title: str
    file_name: str
    index: Optional[int] = None

# --- Main Logic Function ---


def load_and_process_books(file_path: Path) -> List[Book]:
    """
    Reads JSON data using orjson, validates it against the Book model,
    sorts, and indexes the objects.
    """
    logger.info(f"Loading and processing book data from: {file_path}...")
    try:
        with file_path.open('rb') as f:
            data = orjson.loads(f.read())

    except Exception as e:
        logger.exception("FATAL: Could not load or parse the data file.")
        raise

    try:
        book_list = [Book(**item) for item in data]
    except ValidationError as e:
        logger.exception(
            "FATAL: Data validation failed against the Book model.")
        raise

    book_list.sort(key=_get_sort_key)

    for i, book in enumerate(book_list, 1):
        book.index = i

    logger.success(
        f"Successfully loaded and validated {len(book_list)} books into memory.")
    return book_list

# --- Helper Functions ---


def _get_sort_key(book: Book) -> str:
    """Private helper function to return the sorting key for a book object."""
    return book.title.lower() if book.title else ""
