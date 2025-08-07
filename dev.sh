#!/bin/bash

# Stop any running containers
docker-compose down

# Start containers using the development configuration
docker-compose -f docker-compose.dev.yml up -d

echo "Development environment started with auto-reload enabled."
echo "Your code changes will now be reflected without restarting containers."
echo "Access the application at http://localhost:8000"