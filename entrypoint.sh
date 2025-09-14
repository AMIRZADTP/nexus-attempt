#!/bin/sh

echo "Waiting for database to be ready..."
while ! pg_isready -h db -p 5432 -q -U ${DB_USER}; do
  sleep 2
done
echo "Database is ready!"

echo "Running database initialization..."
python -m backend.init_db

echo "Starting Uvicorn server..."
exec "$@"