# Contributing to Nexus Attempt

Thank you for your interest in contributing to Nexus Attempt. This document provides guidelines and information for developers looking to contribute to this local-first knowledge graph application.

## 🏗️ Project Architecture

Nexus Attempt is built with a modern Python stack using FastAPI, SQLAlchemy 2.0, and PostgreSQL. The architecture follows clean separation of concerns:

```
nexus-attempt/
├── backend/                # Core application package
│   ├── server.py           # FastAPI application and routing
│   ├── domain.py           # Business logic and data access layer  
│   ├── database.py         # Database configuration and connection management
│   ├── models.py           # SQLAlchemy ORM models and schema definitions
│   └── templates/          # Jinja2 templates for web interface
├── scripts/                # Database utilities and migration scripts
├── frontend/               # Reserved for future Svelte implementation
├── data_example.json       # Sample dataset template for development
└── docker-compose.yml      # PostgreSQL container orchestration
```

## 🚀 Development Setup

### Prerequisites

- Python 3.10+
- Docker Desktop
- Git

### Environment Configuration

1. **Clone and setup**:
   ```bash
   git clone <repository-url>
   cd nexus-attempt
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # Windows
   # source venv/bin/activate   # Unix-like systems
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment**:
   ```bash
   cp .env.example .env
   # Edit .env with appropriate database credentials
   ```

4. **Configure data file**:
   The application requires a `data.json` file for initial data loading. Use the provided sample:
   1. Copy `data_example.json` to a new file named `data.json`:
      ```bash
      copy data_example.json data.json  # Windows
      # cp data_example.json data.json  # Unix-like
      ```
   2. Edit `data.json` with your specific configuration values (e.g., book titles, file paths).
   3. Ensure `data.json` is placed in the project root directory for the application to locate it.
   Note: Add `data.json` to `.gitignore` if it contains personal data to maintain privacy.

5. **Initialize services**:

4. **Initialize services**:
   ```bash
   docker-compose up -d
   python -m scripts.create_tables
   python -m scripts.migrate_to_db
   ```

5. **Start development server**:
   ```bash
   uvicorn backend.server:app --reload
   ```

## 📋 Development Guidelines

### Code Standards

- **Type Hints**: All functions must include proper type annotations
- **Async/Await**: Use async patterns for all I/O operations
- **Error Handling**: Implement appropriate exception handling
- **Documentation**: Add docstrings for public methods and complex logic

### Database Operations

- **Module Execution**: Always use `python -m scripts.script_name` for database scripts
- **Enum Usage**: Use proper SQLAlchemy enum types (`ItemTypeEnum.BOOK` not `'book'`)
- **SQL Preparation**: Separate multiple SQL commands for PostgreSQL compatibility
- **Transaction Management**: Use appropriate transaction boundaries

### API Development

- **FastAPI Patterns**: Follow FastAPI conventions for dependency injection
- **Response Models**: Use Pydantic models for request/response validation
- **Error Responses**: Return appropriate HTTP status codes and error messages

## 🔄 Contribution Workflow

### Issue Management

1. Search existing issues before creating new ones
2. Use appropriate labels and templates
3. Provide detailed reproduction steps for bugs
4. Include system information and error messages

### Pull Request Process

1. **Branch Strategy**: Create feature branches from `main`
   ```bash
   git checkout -b feature/description-of-feature
   ```

2. **Development**: Implement changes following project conventions

3. **Testing**: Verify functionality locally
   ```bash
   # Test database operations
   python -m scripts.create_tables
   python -m scripts.migrate_to_db  # Uses data.json (copied from data_example.json)
   
   # Test web application
   uvicorn backend.server:app --reload
   ```

4. **Documentation**: Update relevant documentation

5. **Commit Standards**: Use clear, descriptive commit messages
   ```bash
   git commit -m "feat: add search functionality for book titles"
   git commit -m "fix: resolve enum type mismatch in migration script"
   ```

### Code Review

All contributions undergo code review focusing on:
- Architecture and design patterns
- Security considerations
- Performance implications
- Code quality and maintainability
- Documentation completeness

## 🛠️ Technical Considerations

### Import System

The project uses Python's module system with specific patterns:
- Scripts must be executed with `-m` flag for proper import resolution
- Package imports use full path notation (`from backend.models import Item`)

### Database Schema

- Uses SQLAlchemy 2.0 async patterns
- Enum types are strictly enforced
- UUID primary keys for external references
- Timestamp tracking with timezone awareness

### Performance

- Async database operations for non-blocking I/O
- Connection pooling through SQLAlchemy
- Efficient query patterns with proper indexing

## 🔒 Security Guidelines

- Environment variables for sensitive configuration
- No hardcoded credentials in source code
- Proper input validation and sanitization
- SQL injection prevention through ORM usage

## 📚 Documentation

- API documentation auto-generated via FastAPI
- Code documentation through docstrings
- Architecture decisions documented in issues/PRs
- Setup and deployment guides maintained

## 🚨 Troubleshooting

### Common Issues

**Module Import Errors**:
```bash
# Use module execution pattern
python -m scripts.create_tables
```

**Database Connection Issues**:
```bash
# Verify container status
docker ps
docker logs nexus_db
```

**Environment Setup**:
```bash
# Ensure virtual environment activation
.\venv\Scripts\Activate.ps1
pip list  # Verify installed packages
```

## 🎯 Project Roadmap

### Current Phase
- Core CRUD operations for items
- Basic web interface
- PostgreSQL integration
- Docker development environment

### Near Term
- Search and filtering capabilities
- Enhanced API endpoints
- Data validation improvements
- Testing framework integration

### Future Considerations
- Svelte frontend development
- Full-text search implementation
- Multi-user support
- Export/import functionality

## 📞 Support

- **Issues**: Use GitHub issue tracker for bugs and feature requests
- **Discussions**: GitHub Discussions for architecture and design questions
- **Documentation**: Refer to inline code documentation and API docs

## 🏛️ Governance

This project welcomes contributions from developers at all experience levels. Maintainers will:
- Review contributions promptly
- Provide constructive feedback
- Maintain project direction and quality standards
- Foster an inclusive development environment

---

By contributing to Nexus Attempt, you agree to license your contributions under the same terms as the project (MIT License).