Nexus Attempt

A local-first, containerized personal knowledge base, starting with a simple book catalog.

Quick Start

This project is fully containerized using Docker. The only prerequisite is a working installation of Docker and Docker Compose.

1. Clone the Repository

Clone this project to your local machine:
```Bash
git clone https://github.com/your-username/nexus-attempt.git
cd nexus-attempt
```

2. Create Environment File

Create a `.env` file in the project's root directory and paste the following content. The default values are configured for the local Docker environment.
```Code snippet

# PostgreSQL Database Credentials
POSTGRES_USER=nexus_user
POSTGRES_PASSWORD=nassword
POSTGRES_DB=nexus_db

# Application Database Connection Settings
DB_USER=nexus_user
DB_PASSWORD=nassword
DB_HOST=db
DB_PORT=5432
DB_NAME=nexus_db
```

3. Build and Run the Application

Run the following command in your terminal. This will build the application image and start all services in the background.
```bash
docker-compose up --build -d
```
    --build: Builds the application's Docker image from the Dockerfile.

    -d: Runs the containers in detached mode (in the background).


The first time you run this, the entrypoint.sh script will automatically wait for the database to be ready, create all necessary tables, and migrate the initial data from data.json.

4. Access the Application

Once the containers are up and running, open your web browser and navigate to:

http://localhost:8000

You should see the list of books from your `data.json` file.

Additional Commands

Checking Logs

To view the live logs of the application:
```Bash
docker-compose logs -f app
```
Stopping the Application

To stop and remove all containers, networks, and volumes:
```Bash
docker-compose down -v
```