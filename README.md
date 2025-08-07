# Job Portal Backend

A Django-based job portal backend application with Docker support.

## Development Setup

### Quick Start

For development with auto-reload (changes reflect without restarting):

```bash
# Start development environment
./dev.sh
```

Your code changes will automatically be reflected without needing to restart containers.

### Production Setup

For production deployment:

```bash
# Start production environment
./prod.sh
```

Note: In production mode, you need to restart containers when code changes.

## Docker Environments

This project includes two Docker Compose configurations:

1. **Development Environment** (`docker-compose.dev.yml`)
   - Uses Django's built-in development server
   - Auto-reloads when code changes
   - Ideal for active development

2. **Production Environment** (`docker-compose.yml`)
   - Uses Gunicorn for serving the application
   - More performant but requires container restarts for code changes
   - Suitable for production deployment

## Services

- **Web**: Django application
- **Celery Worker**: Background task processing
- **Celery Beat**: Scheduled task management
- **Redis**: Message broker and result backend

## Accessing the Application

- Web Interface: http://localhost:8000
- Admin Panel: http://localhost:8000/admin/
