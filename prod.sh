#!/bin/bash

# Stop any running containers
docker-compose down

# Start containers using the production configuration
docker-compose up -d

echo "Production environment started."
echo "Note: Code changes require restarting containers to take effect."
echo "Access the application at http://localhost:8000"