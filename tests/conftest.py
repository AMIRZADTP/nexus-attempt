from collections.abc import AsyncGenerator

import pytest
from httpx import ASGITransport, AsyncClient

from nexus.main import app


@pytest.fixture
async def client() -> AsyncGenerator[AsyncClient, None]:
    """
    Make a 'client' fixture available to test functions.
    This client is an async httpx client aimed at our 'app'.
    """
    # We use ASGITransport to route requests directly to the FastAPI app
    # in-memory, rather than over a real network socket.
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac
