# Changelog

## Project Evolution Story
Nexus Attempt started as a personal journey to regain control over my data after losing it in previous setups. I began with a Python script called BookUtil to organize my ebooks: renaming files based on chosen titles, filtering them, and generating a JSON file (`data.json`) from a template (`data_example.json`) with title and file_name for each book. This JSON became the primary data source for the database and web app.

Development involved AI tools: A full session with Gemini Pro 2.5 until it crashed and started hallucinating, then fixed using Warp.dev AI IDE until hitting request limits. The goal was a local-first knowledge graph starting with book catalog, emphasizing privacy and offline access.

Semantic versioning:
- v0.1.0: Initial prototype deployed on Railway (main branch).
- v1.0.0: Current version with codebase review improvements, privacy enhancements (data.json.example), and evolution branch.

## v1.0.0 (2025-09-13)
- Added comprehensive codebase review in review.md.
- Privacy enhancement: Created data_example.json with sample entries; full data.json gitignored.
- Updated .gitignore to exclude sensitive data.json.
- Git branching: New v1.0.0-evolution branch for ongoing development, keeping v0.1.0 prototype intact.
- Documentation: This CHANGELOG.md and README.md updates for dual-version deployment.
- Roadmap integration: Prepared for frontend, search, multi-type support.

## v0.1.0 (Initial Prototype)
- Basic FastAPI backend with async PostgreSQL via SQLAlchemy.
- Book catalog from data.json (copied from data_example.json template, 449 items), migration script.
- Docker-compose for DB, Jinja2 templates for web UI.
- Deployed on Railway linked to main/master branch.
- Core CRUD (read) for items, API docs at /docs.