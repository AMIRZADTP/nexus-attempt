FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen --no-install-project --no-dev

# Copy application code
COPY . .

# Install the application itself
RUN uv sync --frozen --no-dev

# Make entrypoint executable
RUN chmod +x /app/entrypoint.sh

# Create user
RUN useradd --create-home --shell /bin/bash appuser

# Add virtual environment to PATH
ENV PATH="/app/.venv/bin:$PATH"

USER appuser

EXPOSE 8000
ENTRYPOINT ["/app/entrypoint.sh"]
# CMD is handled by entrypoint calling exec uvicorn if arguments are passed, 
# but we hardcoded uvicorn in entrypoint for simplicity or we can keep it flexible.
# The updated entrypoint.sh executes uvicorn directly.
# So CMD here is not strictly needed if ENTRYPOINT runs uvicorn, but standard practice:
CMD []