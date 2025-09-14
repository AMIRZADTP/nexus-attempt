import configparser
from pathlib import Path
from typing import List

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, ORJSONResponse
from fastapi.templating import Jinja2Templates
from loguru import logger

from .core import Book, load_and_process_books

# --- Configuration & Initial Setup ---

config = configparser.ConfigParser()
config.read('config.ini')

log_path = config['Paths']['log_file']
json_path = Path(config['Paths']['json_input'])

logger.add(log_path, rotation="10 MB", level="INFO", encoding="utf-8")
logger.add(lambda msg: print(msg, end=""), level="INFO", colorize=True)

# --- FastAPI App Initialization ---

app = FastAPI(default_response_class=ORJSONResponse)
templates = Jinja2Templates(directory="nexus_attempt/templates")

# --- In-Memory Data Loading ---

try:
    BOOKS_IN_MEMORY: List[Book] = load_and_process_books(json_path)
except Exception:
    logger.critical("Application startup failed: Could not load book data.")
    BOOKS_IN_MEMORY = []

# --- Endpoints ---


@app.get("/health")
async def health():
    """Health check endpoint for deployment verification."""
    return {"status": "ok", "books_count": len(BOOKS_IN_MEMORY)}

@app.get("/", response_class=HTMLResponse)
async def show_books_list(request: Request):
    """Displays the list of all books directly from memory."""
    return templates.TemplateResponse("book_list.html", {"request": request, "books": BOOKS_IN_MEMORY})


@app.get("/books/{book_id}", response_class=HTMLResponse)
async def show_book_detail(request: Request, book_id: int):
    """Finds and displays a single book from memory by its index."""
    book_to_show = next(
        (book for book in BOOKS_IN_MEMORY if book.index == book_id), None)

    if book_to_show:
        return templates.TemplateResponse("book_detail.html", {"request": request, "book": book_to_show})
    else:
        raise HTTPException(
            status_code=404, detail=f"Book with index {book_id} not found.")
