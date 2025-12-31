import uuid
from pathlib import Path

from fastapi import APIRouter, Depends, HTTPException, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession

from nexus.api.deps import get_db_session
from nexus.domain.services import fetch_all_items, fetch_item_by_uuid
from nexus.domain.schemas import ItemDetail

router = APIRouter()

# Locate templates directory relative to the project root or this package
# For now, assuming templates are at standard location relative to backend/original or root
# With the move to src/nexus, templates might still be at root/backend/templates or root/templates
# The mv commands didn't move templates. They are in `backend/templates`.
# I should move them to `src/nexus/templates` or `templates/`.
# Let's assume user will move them or I will. Let's point to `src/nexus/templates` for now
# or better `.../nexus-attempt/templates`.
# Let's verify where existing templates are: `backend/templates`.
# I will define path relative to __file__ which is `src/nexus/api/routes/pages.py`
# so parent.parent.parent.parent / "backend" / "templates"?
# No, we should move templates to `src/nexus/templates`.
# I'll code it for `src/nexus/templates` and move them later.

templates_dir = Path(__file__).resolve().parent.parent.parent / "templates"
templates = Jinja2Templates(directory=templates_dir)


@router.get("/", response_class=HTMLResponse)
async def get_items_view(
    request: Request,
    db_session: AsyncSession = Depends(get_db_session),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
):
    skip = (page - 1) * page_size
    items = await fetch_all_items(db_session, skip=skip, limit=page_size)
    return templates.TemplateResponse(
        "book_list.html",
        {"request": request, "books": items, "page": page, "page_size": page_size},
    )


@router.get("/books/{item_uuid}", response_class=HTMLResponse)
async def get_item_detail_view(
    request: Request,
    item_uuid: uuid.UUID,
    db_session: AsyncSession = Depends(get_db_session),
):
    item_model = await fetch_item_by_uuid(db_session, item_uuid=item_uuid)
    if not item_model:
        raise HTTPException(status_code=404, detail="Item not found.")
    item_detail = ItemDetail.model_validate(item_model)
    return templates.TemplateResponse(
        "book_detail.html", {"request": request, "book": item_detail}
    )
