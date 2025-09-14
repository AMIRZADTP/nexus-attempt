import uuid
from fastapi import FastAPI, Request, HTTPException, Depends, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncGenerator
from pathlib import Path

from .database import SessionLocal
from .domain import fetch_all_items, fetch_item_by_uuid, ItemDetail

app = FastAPI()
templates = Jinja2Templates(directory=Path(
    __file__).resolve().parent / "templates")


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session


@app.get("/", response_class=HTMLResponse)
async def get_items_view(
    request: Request,
    db_session: AsyncSession = Depends(get_db_session),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100)
):
    skip = (page - 1) * page_size
    items = await fetch_all_items(db_session, skip=skip, limit=page_size)
    return templates.TemplateResponse(
        "book_list.html",
        {"request": request, "books": items, "page": page, "page_size": page_size}
    )


@app.get("/books/{item_uuid}", response_class=HTMLResponse)
async def get_item_detail_view(request: Request, item_uuid: uuid.UUID, db_session: AsyncSession = Depends(get_db_session)):
    item_model = await fetch_item_by_uuid(db_session, item_uuid=item_uuid)
    if not item_model:
        raise HTTPException(status_code=404, detail="Item not found.")
    item_detail = ItemDetail.model_validate(item_model)
    return templates.TemplateResponse("book_detail.html", {"request": request, "book": item_detail})
