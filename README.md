# Nexus 2.0 🚀

A **local-first, clean-architecture knowledge base**, engineered for performance, testability, and long-term maintainability.

---

## 🏗️ Clean Architecture

Nexus follows strict **Decoupling** and **Dependency Inversion** principles.

| Layer | Path | Purpose | Dependency Flow |
|-------|------|---------|-----------------|
| **Interface** | `src/nexus/interface` | FastAPI routes, templates, static assets. | `Interface` -> `Application` |
| **Application**| `src/nexus/application` | Business use cases and orchestration logic. | `Application` -> `Domain` |
| **Domain** | `src/nexus/domain` | **Pure Python** entities and repository interfaces. | **Independent** |
| **Infrastructure**| `src/nexus/infrastructure` | Database (Postgres), Cache (In-memory), Repositories. | `Infrastructure` -> `Domain` |

---

## 🛠️ Hybrid Development Workflow

To maximize speed and reliability, we use a hybrid approach: **Docker for Infrastructure** and **Local Python for Logic**.

### 1. Prerequisites
- **Docker Desktop** (ensure WSL 2 backend is enabled on Windows).
- **uv** (the fastest Python package manager).

### 2. The Development Mode (Fast)
Spin up only the database in the background:
```bash
docker-compose up -d db
```
Run the app locally for instant reloads and easy debugging:
```bash
uv sync --all-extras
uv run uvicorn nexus.main:app --reload
```
Access the app at: **[http://localhost:8000](http://localhost:8000)**

### 3. The Isolated Mode (Safe/Pre-deployment)
To test the full containerized environment without stopping your local work:
```bash
# Force recreate ensures the port mapping 8800:8000 is applied
docker-compose up -d --build
```
Access the isolated app at: **[http://localhost:8800](http://localhost:8800)**

| Environment | Host Port | Purpose |
|-------------|------------|---------|
| **Local (uv)** | `8000` | Active coding & debugging. |
| **Docker** | `8800` | Pre-deployment verification. |

---

## 💡 Troubleshooting & Mastery Tips

### Managing Zombie Processes
If port 8000 or 8800 is "stuck" even after closing the terminal:
1. **Windows**: Kill the ghost process:
   ```powershell
   Get-NetTCPConnection -LocalPort 8000 | Select-Object -ExpandProperty OwningProcess | ForEach-Object { Stop-Process -Id $_ -Force }
   ```
2. **WSL/Docker**: If the above fails, restart the subsystem:
   ```powershell
   wsl --shutdown
   ```

### Managing Containers
- **Stop only the app**: `docker-compose stop app` (keeps DB alive).
- **Start only the app**: `docker-compose start app`.
- **Full Cleanup**: `docker-compose down` (Removes everything).

---

## 🛡️ Quality Gates

Every change must pass our strict quality checks:
```bash
uv run ruff check .
uv run mypy .
uv run pytest
```

---

## 📝 Governance

- **ADRs**: See [ADR 001: Clean Architecture](reports/ADR_001_clean_architecture.md).
- **History**: Audit logs and linting results are in the `/reports` directory.
- **Roadmap**: Progress is tracked in `task.md`.