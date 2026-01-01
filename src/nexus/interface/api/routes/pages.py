import uuid
from pathlib import Path

from fastapi import APIRouter, Depends, HTTPException, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession

from nexus.interface.api.deps import get_db_session
from nexus.domain.schemas import ItemDetail
from nexus.application.services import ItemService
from nexus.infrastructure.persistence.repositories import SqlAlchemyItemRepository

router = APIRouter()

templates_dir = Path(__file__).resolve().parent.parent.parent.parent / "templates"
templates = Jinja2Templates(directory=templates_dir)


def get_service(db_session: AsyncSession) -> ItemService:
    repo = SqlAlchemyItemRepository(db_session)
    return ItemService(repo)


@router.get("/", response_class=HTMLResponse)
async def get_items_view(
    request: Request,
    db_session: AsyncSession = Depends(get_db_session),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
) -> HTMLResponse:
    service = get_service(db_session)
    skip = (page - 1) * page_size
    items = await service.list_items(skip=skip, limit=page_size)
    return templates.TemplateResponse(
        "book_list.html",
        {"request": request, "books": items, "page": page, "page_size": page_size},
    )


@router.get("/books/{item_uuid}", response_class=HTMLResponse)
async def get_item_detail_view(
    request: Request,
    item_uuid: uuid.UUID,
    db_session: AsyncSession = Depends(get_db_session),
) -> HTMLResponse:
    service = get_service(db_session)
    item = await service.get_item(item_uuid=item_uuid)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found.")
    
    # Check if we need to convert Entity -> Schema (ItemDetail)
    # ItemDetail expects fields like 'id' (int). Our Entity has 'id' (optional).
    # If Entity.id is None (not fetched?), schema validation might fail if required.
    # Our Repository maps from ORM, so ID should be populated.
    item_detail = ItemDetail.model_validate(item)
    return templates.TemplateResponse(
        "book_detail.html", {"request": request, "book": item_detail}
    )
