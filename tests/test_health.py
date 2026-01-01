import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_root_page_loads(client: AsyncClient) -> None:
    """
    Sanity check: Ensure the application root responds with 200 OK.
    """
    response = await client.get("/")
    assert response.status_code == 200
    # Simple check to ensure we got HTML back
    assert "<html" in response.text.lower()
