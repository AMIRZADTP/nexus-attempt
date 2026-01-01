```.
|-- .dockerignore
|-- .env
|-- .github
|   `-- workflows
|       `-- ci.yml        <-- CI Pipeline
|-- .gitignore
|-- Dockerfile
|-- README.md
|-- data.json
|-- docker-compose.yml
|-- entrypoint.sh
|-- pyproject.toml
|-- reports               <-- Lint reports moved here
|   |-- mypy_errors_utf8.txt
|   |-- mypy_final_err.txt
|   |-- mypy_out.txt
|   |-- mypy_report.txt
|   |-- ruff_out.txt
|   `-- ruff_report.txt
|-- src
|   `-- nexus
|       |-- __init__.py
|       |-- application   <-- Business Logic
|       |   `-- services.py
|       |-- domain        <-- Pure Entities & Interfaces
|       |   |-- __init__.py
|       |   |-- entities.py
|       |   |-- repositories.py
|       |   `-- schemas.py
|       |-- infrastructure <-- Adapters (DB, Cache)
|       |   |-- __init__.py
|       |   |-- cache
|       |   |   `-- memory.py
|       |   |-- init_db.py
|       |   `-- persistence
|       |       |-- database.py
|       |       |-- models.py
|       |       `-- repositories.py
|       |-- interface      <-- Web API
|       |   `-- api
|       |       |-- __init__.py
|       |       |-- deps.py
|       |       `-- routes
|       |           |-- __init__.py
|       |           `-- pages.py
|       |-- main.py
|       |-- static
|       |   |-- swagger-ui-bundle.js
|       |   `-- swagger-ui.css
|       `-- templates
|           |-- book_detail.html
|           `-- book_list.html
|-- tests
|   |-- conftest.py
|   |-- test_health.py
|   `-- unit
|       `-- domain
|           `-- test_entities.py
`-- uv.lock```