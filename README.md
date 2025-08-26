# Nexus Attempt (v0.1.0)

A lightweight and high-performance web application for displaying and browsing a curated book collection. Built with Python, FastAPI, and a modern, modular architecture.

## Architecture

This project follows a clean, modular architecture that separates the web interface from the core application logic, making it scalable and easy to maintain.

-   `/nexus-attempt/`: The main project and Git repository root.
    -   `venv/`: The isolated Python virtual environment for managing dependencies.
    -   `config.ini`: The configuration file for defining file paths.
    -   `data.json`: The input data file containing the book list.
    -   `requirements.txt`: A list of all Python dependencies for the project.
    -   `/nexus_attempt/`: The main Python package containing the application's source code.
        -   `main.py`: The FastAPI web server, responsible for handling HTTP requests and rendering HTML pages.
        -   `core.py`: The core logic module, which includes the Pydantic data model (`Book`) and data processing functions.
        -   `/templates/`: Contains the Jinja2 HTML templates for the user interface.

## Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

-   Python 3.10 or newer
-   `pip` package manager

### Installation

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/your-username/nexus-attempt.git](https://github.com/your-username/nexus-attempt.git)
    cd nexus-attempt
    ```

2.  **Set Up the Virtual Environment**

    This project requires a virtual environment to manage its dependencies in isolation.

    * Create the environment:
        ```bash
        python -m venv venv
        ```
    * Activate the environment:
        * On Windows (PowerShell):
            ```bash
            .\venv\Scripts\Activate.ps1
            ```
        * On macOS & Linux:
            ```bash
            source venv/bin/activate
            ```
    Your terminal prompt should now be prefixed with `(venv)`.

3.  **Install Dependencies**

    Once the virtual environment is active, install all required packages using the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

## Usage

There are two ways to run the application: for local development and for production. Ensure your virtual environment is active for both.

### For Development

This method uses Uvicorn's built-in reloader, which automatically restarts the server when you change your code. This is ideal for development.

```bash
uvicorn nexus_attempt.main:app --reload
```
The server will be running on http://127.0.0.1:8000.

### For Production

This method uses Gunicorn to manage Uvicorn workers, providing a stable and performant server suitable for a live environment. This is the command used by platforms like Render.
```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker nexus_attempt.main:app
```
The application will be served on a port managed by Gunicorn, typically 8000.