#!/bin/bash
set -o errexit  # Exit on error

# Install dependencies
pip install -r requirements.txt

# Navigate to Django project directory
cd pos

# Collect static files
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate

# Create superuser if environment variable is set
if [[ $CREATE_SUPERUSER == "1" ]]; then
    python manage.py createsuperuser --no-input --email "$DJANGO_SUPERUSER_EMAIL"
fi
