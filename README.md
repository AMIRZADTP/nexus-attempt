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
        -   `main.py`: The FastAPI web server.
        -   `core.py`: The core logic and data models.
        -   `/templates/`: Jinja2 HTML templates for the UI.

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

    * First, create the environment:
        ```bash
        python -m venv venv
        ```
    * Next, **activate** the environment. This is a crucial step.
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

### Usage

To run the development web server, ensure your virtual environment is active and then execute the following command from the project's root directory:

```bash
uvicorn nexus_attempt.main:app --reload