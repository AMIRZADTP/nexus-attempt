from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from nexus.interface.api.routes import pages

app = FastAPI(title="Nexus", version="2.0.0-alpha", docs_url=None, redoc_url=None)

# Mount static files
app.mount("/static", StaticFiles(directory="src/nexus/static"), name="static")

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html() -> HTMLResponse:
    from fastapi.openapi.docs import get_swagger_ui_html
    return get_swagger_ui_html(
        openapi_url=app.openapi_url or "/openapi.json",
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
    )

# Include routers
app.include_router(pages.router)
