from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from nexus.api.routes import pages

app = FastAPI(title="Nexus", version="2.0.0-alpha")

# Mount static files if/when we have them (e.g. for htmx)
# app.mount("/static", StaticFiles(directory="static"), name="static")

# Include routers
app.include_router(pages.router)
