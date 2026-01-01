# Nexus

A **local-first, containerized personal knowledge base**, designed to organize your digital life.
Currently features a book catalog with a modern, layered architecture.

## 🚀 Quick Start

### Prerequisites
- **Docker** and **Docker Compose** installed & running.
- **Git** installed.

### 1. Clone & Setup

```bash
git clone https://github.com/your-username/nexus-attempt.git
cd nexus-attempt

# Create environment file
cp .env .env.local  # Or just create .env
```

**Recommended `.env` content:**
```ini
POSTGRES_USER=nexus_user
POSTGRES_PASSWORD=nassword
POSTGRES_DB=nexus_db

DB_USER=nexus_user
DB_PASSWORD=nassword
DB_HOST=localhost
DB_PORT=5432
DB_NAME=nexus_db
```

### 2. Run with Docker

```bash
docker-compose up --build
```
Access the app at: **http://localhost:8000**

---

## 🛠️ Development (Local)

This project uses **uv** for blazing fast dependency management.

### 1. Install `uv`
```powershell
# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Install Dependencies
```bash
uv sync --all-extras
```

### 3. Run Locally
You need a running database first (e.g. via Docker):
```bash
docker-compose up -d db
```

Then run the app:
```bash
uv run uvicorn nexus.main:app --reload
```

### 4. Code Quality
```bash
# Linting & Formatting
uv run ruff check src/
uv run ruff format src/

# Type Checking
uv run mypy src/
```

---

## 🏗️ Architecture

Nexus follows a **Domain-Driven Design (DDD)** inspired layered architecture:

| Layer | Path | Purpose |
|-------|------|---------|
| **Interface** | `src/nexus/interface` | Web API (FastAPI), Routes, Dependencies |
| **Application** | `src/nexus/application` | Business Logic / Orchestration Services |
| **Domain** | `src/nexus/domain` | Pure Business Entities & Abstract Repositories |
| **Infrastructure** | `src/nexus/infrastructure` | Database (Persistence), Adapters |

key Technologies:
- **FastAPI**: Modern, fast web framework
- **SQLAlchemy (Async)**: Database ORM
- **PostgreSQL**: Robust relational database
- **Jinja2**: Server-side templating
- **aiocache**: In-memory caching for performance