# Use an official Python runtime as the base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies if needed (e.g., for any native libs, but minimal here)
# If no dependencies are needed, just update and clean up
RUN apt-get update && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .

# Create a non-root user for security
RUN useradd --create-home appuser
USER appuser

# Expose the port the app runs on
EXPOSE 8080

# Run the application
CMD ["uvicorn", "nexus_attempt.main:app", "--host", "0.0.0.0", "--port", "8080"]