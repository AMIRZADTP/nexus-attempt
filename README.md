# Nexus Attempt

<div align="center">

[![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/) [![Framework](https://img.shields.io/badge/FastAPI-0.111.0-green.svg)](https://fastapi.tiangolo.com/) [![Database](https://img.shields.io/badge/PostgreSQL-17-blue.svg)](https://www.postgresql.org/) [![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)](LICENSE)

_A local-first, high-performance personal knowledge graph, built with a modern, API-driven architecture._

</div>

---

## About

Nexus Attempt is a personal knowledge management system designed to organize and connect digital information. Currently functioning as a book catalog with 449 indexed items, the architecture is built to evolve into a comprehensive knowledge graph for managing bookmarks, notes, articles, and more.

**Core Philosophy**: Your data belongs to you and should reside on your machine, accessible through a fast and powerful interface.

### Built With

- [FastAPI](https://fastapi.tiangolo.com/): High-performance async web server
- [SQLAlchemy 2.0](https://www.sqlalchemy.org/): Modern async ORM
- [PostgreSQL](https://www.postgresql.org/): Reliable relational database
- [Docker](https://www.docker.com/): Containerized database environment
- [Pydantic](https://docs.pydantic.dev/): Data validation and API modeling

---

## Project Structure

```
nexus-attempt/
├── backend/                # Core application package
│   ├── __init__.py         # Package marker
│   ├── server.py           # FastAPI web server and API endpoints
│   ├── domain.py           # Business logic and data access functions
│   ├── database.py         # Database connection and session management
│   ├── models.py           # SQLAlchemy ORM data models and schema
│   └── templates/          # Jinja2 HTML templates for web interface
├── frontend/               # Reserved for future Svelte frontend
│   ├── README.md           # Frontend development notes
│   ├── package.json        # Node.js dependencies (placeholder)
│   ├── jsconfig.json       # JavaScript configuration
│   └── tsconfig.json       # TypeScript configuration
├── scripts/                # Database utilities and migration tools
│   ├── create_tables.py    # Creates database schema from models
│   └── migrate_to_db.py    # Populates database with initial dataset
├── data.json               # Initial dataset (449 books for development)
├── docker-compose.yml      # PostgreSQL container orchestration
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variables template
├── .gitignore              # Git exclusion rules
├── LICENSE                 # MIT license
├── CONTRIBUTING.md         # Development guidelines
└── venv/                   # Python virtual environment
```

### File Descriptions

#### Backend Components

**`backend/server.py`** - FastAPI Application
- Defines web routes and API endpoints
- Handles HTTP requests for book listing and details
- Implements dependency injection for database sessions
- Serves Jinja2 templates for web interface

**`backend/models.py`** - Database Schema
- Defines SQLAlchemy ORM models (Item, Topic, associations)
- Implements ItemTypeEnum for type safety
- Establishes relationships between items and topics
- Configures UUID-based primary keys and timestamps

**`backend/database.py`** - Database Management
- Configures async PostgreSQL connection
- Creates SQLAlchemy engine and session factory
- Manages connection pooling and lifecycle

**`backend/domain.py`** - Business Logic
- Contains data access layer functions
- Implements item fetching and querying logic
- Defines Pydantic models for API responses
- Handles data transformation between database and API

#### Database Scripts

**`scripts/create_tables.py`** - Schema Creation
- Drops and recreates database schema
- Creates all tables defined in models.py
- Handles enum type creation in PostgreSQL

**`scripts/migrate_to_db.py`** - Data Migration
- Reads initial data from data.json
- Populates database with book records
- Handles data transformation and validation

#### Configuration Files

**`data.json`** - Initial Dataset
- Contains 449 book records for development
- Includes titles, filenames, and metadata
- Used by migration script to seed database

**`docker-compose.yml`** - Container Configuration
- Defines PostgreSQL service configuration
- Sets up persistent data volumes
- Configures environment variable injection

**`requirements.txt`** - Python Dependencies
- Lists all required Python packages
- Includes web framework, database, and utility libraries

---

## Quick Start

### Prerequisites

- Python 3.10 or newer
- Docker Desktop (must be running)
- Git

### Installation

1. **Clone and setup**:
   ```bash
   git clone <repository-url>
   cd nexus-attempt
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # Windows PowerShell
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment**:
   ```bash
   cp .env.example .env
   # Edit .env with your desired PostgreSQL password
   ```

4. **Start database**:
   ```bash
   docker-compose up -d
   ```

5. **Initialize database**:
   ```bash
   python -m scripts.create_tables
   python -m scripts.migrate_to_db
   ```

6. **Start development server**:
   ```bash
   uvicorn backend.server:app --reload
   ```

7. **Access application**:
   - Web interface: http://127.0.0.1:8000
   - API documentation: http://127.0.0.1:8000/docs

---

## Development

### Key Concepts

**Module Execution**: Scripts must be run using `python -m scripts.script_name` to ensure proper import resolution from the project root.

**Async Architecture**: All database operations use async/await patterns for non-blocking I/O performance.

**Type Safety**: Enum types are strictly enforced (use `ItemTypeEnum.BOOK` not `'book'`).

### Development Commands

```bash
# Database management
docker-compose up -d                 # Start PostgreSQL
python -m scripts.create_tables      # Reset database schema  
python -m scripts.migrate_to_db      # Populate with data

# Server management
uvicorn backend.server:app --reload  # Development server (hot reload)
uvicorn backend.server:app           # Production-like server
```

### Architecture Notes

The application follows a three-tier architecture:
1. **Presentation Layer**: FastAPI routes and Jinja2 templates
2. **Business Layer**: Domain logic in `domain.py`
3. **Data Layer**: SQLAlchemy models and database operations

---

## API Endpoints

- `GET /` - List all books with pagination
- `GET /books/{uuid}` - Get detailed information for a specific book
- `GET /docs` - Interactive API documentation

---

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for:
- Development setup instructions
- Coding standards and guidelines
- Pull request process
- Architecture considerations

---

## Roadmap

### Current Phase
- ✅ Core CRUD operations for items
- ✅ Basic web interface
- ✅ PostgreSQL integration
- ✅ Docker development environment

### Near Term
- [ ] Search and filtering capabilities
- [ ] Enhanced API endpoints
- [ ] Data validation improvements
- [ ] Testing framework integration

### Future Vision
- [ ] Svelte frontend development
- [ ] Full-text search implementation
- [ ] Multi-type content support (bookmarks, notes)
- [ ] Export/import functionality

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Technical Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| Web Framework | FastAPI | Async HTTP server and API |
| Database | PostgreSQL 17 | Data persistence |
| ORM | SQLAlchemy 2.0 | Database abstraction |
| Containerization | Docker | Development environment |
| Validation | Pydantic | Data modeling and validation |
| Templates | Jinja2 | Server-side rendering |