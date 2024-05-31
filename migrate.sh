#!/bin/bash
set -e  # Exit on any error

DJANGO_SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL="username@example.com"}
cd /app/

/opt/venv/bin/python manage.py migrate --noinput 

/opt/venv/bin/python manage.py createsuperuser --email $DJANGO_SUPERUSER_EMAIL --noinput || true

/opt/venv/bin/python manage.py collectstatic --noinput


echo "Static files collected:"
ls  -r /app/staticfiles


