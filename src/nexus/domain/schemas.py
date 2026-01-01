import uuid

from pydantic import BaseModel, ConfigDict, field_validator


class ItemSummary(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    uuid: uuid.UUID
    title: str


class ItemDetail(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    uuid: uuid.UUID
    title: str
    source: str | None = None
    item_type: str
    attributes: dict | None = None
    created_at: str

    @field_validator('created_at', mode='before')
    def format_date(cls, v: object) -> str:
        if v and hasattr(v, 'strftime'):
            return v.strftime('%Y-%m-%d %H:%M')  # type: ignore
        return "N/A"
