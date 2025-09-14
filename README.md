# Nexus Attempt

<div align="center">

[![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/) [![Framework](https://img.shields.io/badge/FastAPI-0.111.0-green.svg)](https://fastapi.tiangolo.com/) [![Database](https://img.shields.io/badge/PostgreSQL-17-blue.svg)](https://www.postgresql.org/) [![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)](LICENSE)

_A local-first, high-performance personal knowledge graph, built with a modern, API-driven architecture._

</div>

---

## About

Nexus Attempt is a personal knowledge management system designed to organize and connect digital information. It starts as a book catalog with 449 indexed items and is built to evolve into a comprehensive knowledge graph supporting bookmarks, notes, articles, and more.

**Core Philosophy**: Your data belongs to you, stored locally and accessible via a fast, intuitive interface.

See [CHANGELOG.md](CHANGELOG.md) for updates, versioning, and history.

### Built With

- [FastAPI](https://fastapi.tiangolo.com/): High-performance async web framework
- [SQLAlchemy 2.0](https://www.sqlalchemy.org/): Modern async ORM
- [PostgreSQL](https://www.postgresql.org/): Reliable relational database
- [Docker](https://www.docker.com/): Containerized environments
- [Pydantic](https://docs.pydantic.dev/): Data validation and modeling
- [Jinja2](https://jinja.palletsprojects.com/): Server-side templating

---

## Project Structure

```
nexus-attempt/
├── nexus_attempt/            # Core application package
│   ├── __init__.py           # Package initializer
│   ├── main.py               # FastAPI app and routes
│   ├── core.py               # Business logic and data models
│   └── templates/            # HTML templates (Jinja2)
│       ├── book_list.html
│       └── book_detail.html
├── config.ini                # Configuration file
├── data.json                 # Initial data source
├── requirements.txt          # Python dependencies
├── Dockerfile                # Docker image definition
├── .dockerignore             # Docker build exclusions
├── .gitignore                # Git exclusions
├── README.md                 # Project documentation
└── LICENSE                   # MIT license
```

### Key Files

- **`nexus_attempt/main.py`**: Defines the FastAPI app, routes, and template rendering.
- **`nexus_attempt/core.py`**: Handles data processing, Pydantic models (e.g., Book), and logic.
- **`config.ini`**: Stores paths and settings (e.g., data file location).
- **`data.json`**: JSON file with book data; customize for your collection.
- **`Dockerfile`**: Builds a containerized version for easy deployment.

---

## Quick Start

### Prerequisites

- Python 3.10+
- Docker (for database/containerized runs)
- Git

### Local Installation and Run

1. **Clone the Repository**:
   ```
   git clone https://github.com/AMIRZADTP/nexus-attempt.git
   cd nexus-attempt
   ```

2. **Set Up Virtual Environment**:
   ```
   python -m venv venv
   # Activate:
   # Windows: venv\Scripts\activate
   # macOS/Linux: source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Configure Data**:
   - Edit `config.ini` for data paths if needed.
   - Ensure `data.json` contains your book data (format: array of objects with title, author, etc.).
   - Add `data.json` to `.gitignore` for privacy.

5. **Run the Application**:
   - For development (with auto-reload):
     ```
     uvicorn nexus_attempt.main:app --reload --host 127.0.0.1 --port 8000
     ```
   - For production-like (bind to all interfaces):
     ```
     uvicorn nexus_attempt.main:app --host 0.0.0.0 --port 8000
     ```
   - Access: http://localhost:8000 (web UI), http://localhost:8000/docs (API docs).

### Docker Run (Local)

1. **Build the Image**:
   ```
   docker build -t nexus-attempt .
   ```

2. **Run the Container**:
   ```
   docker run -p 8000:8080 nexus-attempt
   ```
   - Maps host port 8000 to container port 8080.
   - Access: http://localhost:8000

Troubleshooting Local Runs:
- Ensure `data.json` is valid JSON.
- Check console for import errors (e.g., missing dependencies).
- If port 8000 is in use, change `--port` flag.

---

## Deployment

For deploying to cloud platforms (e.g., PaaS like Heroku, Render, or container services), use these general instructions. Adapt based on the platform's runtime (Python or Docker).

### Platform-Agnostic Deployment (Non-Docker)

1. **Prepare Files**:
   - Ensure `requirements.txt` is up-to-date.
   - Create a `Procfile` (for Procfile-based platforms):
     ```
     web: uvicorn nexus_attempt.main:app --host 0.0.0.0 --port $PORT
     ```
     - `$PORT` is set by the platform (e.g., 8000).
   - For Gunicorn (production scaling):
     - Add `gunicorn` to `requirements.txt`.
     - Procfile: `web: gunicorn -w 4 -k uvicorn.workers.UvicornWorker nexus_attempt.main:app`

2. **Environment Configuration**:
   - Set vars like `DATA_PATH` in platform dashboard (point to `data.json`).
   - Upload `data.json` securely (e.g., via platform file storage).

3. **Deploy Steps**:
   - Connect Git repo to platform.
   - Select Python runtime.
   - Set build command: `pip install -r requirements.txt`
   - Set start command: Use Procfile or direct `uvicorn nexus_attempt.main:app --host 0.0.0.0 --port $PORT`
   - Deploy and monitor logs for errors.

### Docker-Based Deployment

1. **Build and Push Image**:
   - Build: `docker build -t yourusername/nexus-attempt:latest .`
   - Push to registry (e.g., Docker Hub): `docker push yourusername/nexus-attempt:latest`

2. **Platform Setup**:
   - Choose Docker runtime.
   - Specify image: `yourusername/nexus-attempt:latest`
   - Set port: 8080 (exposed in Dockerfile).
   - Configure env vars and volumes for `data.json` if persistent storage needed.

Troubleshooting Deployment:
- Logs: Check for missing files (e.g., `data.json` not found) or port binding errors.
- Dependencies: Ensure all in `requirements.txt`.
- Data: Use platform storage for `data.json`; avoid committing sensitive data.
- Scaling: Use Gunicorn for multi-worker support.

---

## Liara-Specific Deployment

Liara is a cloud PaaS supporting Git and Docker deployments. Follow these steps for seamless setup.

### Prerequisites

- Liara account (sign up at liara.ir).
- Git repo pushed (with Dockerfile if using containers).
- `data.json` prepared (upload via Liara console if needed).

### Step-by-Step Guide

1. **Create App in Liara Console**:
   - Log in to Liara dashboard.
   - Click "New App" > Select "Git" (for source code) or "Docker" (for image).
   - Connect your GitHub repo (https://github.com/AMIRZADTP/nexus-attempt).

2. **Configure Runtime**:
   - For Git (Python runtime):
     - Runtime: "Python".
     - Build Command: `pip install -r requirements.txt`
     - Start Command: `uvicorn nexus_attempt.main:app --host 0.0.0.0 --port $PORT`
     - Or use Procfile (create in root):
       ```
       web: uvicorn nexus_attempt.main:app --host 0.0.0.0 --port $PORT
       ```
   - For Docker:
     - Runtime: "Docker".
     - Liara auto-builds from Dockerfile on Git push.
     - Port: 8080 (matches EXPOSE in Dockerfile).

3. **Environment Variables and Files**:
   - In "Config" tab: Add vars (e.g., `DATA_PATH=/app/data.json`).
   - Upload `data.json`: Use "Files" tab or persistent disk (add to liara.json if needed):
     ```json
     {
       "type": "python:uvicorn",
       "disk": 512,
       "cmd": "uvicorn nexus_attempt.main:app --host 0.0.0.0 --port $PORT"
     }
     ```
   - For config.ini: Upload or set via env vars.

4. **Deploy**:
   - Click "Deploy".
   - Monitor build/logs in "Logs" tab.
   - Access via assigned domain (e.g., yourapp.liara.ir).

### Troubleshooting on Liara

- **Build Fails**: Check logs for missing deps; ensure requirements.txt is complete.
- **Start Command Rejected**: Use Procfile or liara.json instead of direct command.
- **Data Not Loading**: Verify `data.json` path in config.ini; use absolute paths (/app/data.json).
- **Port Issues**: Liara uses $PORT; ensure --port $PORT in command.
- **Persistence**: Enable disk in config for `data.json` storage across deploys.
- **Logs**: View real-time logs; common errors: Import failures (check Python version), file not found (upload data).
- **Scaling**: Liara auto-scales; add workers with Gunicorn if traffic high.

Contact Liara support for platform-specific issues.

---

## API Endpoints

- `GET /` - Book list (paginated)
- `GET /books/{id}` - Book details
- `GET /docs` - Interactive API docs (Swagger)

---

## Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines, setup, and pull request process.

---

## License

MIT License - see [LICENSE](LICENSE).