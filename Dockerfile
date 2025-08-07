# Dockerfile

FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=job_portal.settings

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt .
RUN apt-get update && apt-get install -y curl && \
    pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . .

# Default command
CMD python manage.py migrate && python manage.py collectstatic --noinput && gunicorn job_portal.wsgi:application --bind 0.0.0.0:8000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/ || exit 1
