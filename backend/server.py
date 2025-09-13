import uuid
from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncGenerator
from pathlib import Path

from .domain import fetch_all_items, fetch_item_by_uuid, ItemDetail
from .database import AsyncSessionFactory

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()
templates = Jinja2Templates(directory=BASE_DIR / "templates")


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionFactory() as session:
        yield session


@app.get("/", response_class=HTMLResponse)
async def get_items_view(request: Request, db_session: AsyncSession = Depends(get_db_session)):
    items = await fetch_all_items(db_session)
    return templates.TemplateResponse("book_list.html", {"request": request, "books": items})


@app.get("/books/{item_uuid}", response_class=HTMLResponse)
async def get_item_detail_view(request: Request, item_uuid: uuid.UUID, db_session: AsyncSession = Depends(get_db_session)):
    item_model = await fetch_item_by_uuid(db_session, item_uuid=item_uuid)
    if not item_model:
        raise HTTPException(status_code=404, detail="Item not found.")

    item_detail = ItemDetail.model_validate(item_model)
    return templates.TemplateResponse("book_detail.html", {"request": request, "book": item_detail})
