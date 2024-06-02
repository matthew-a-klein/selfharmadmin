#!/bin/bash
DJANGO_SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL="matthewklein345@gmail.com"}
cd /app/

/opt/venv/bin/python manage.py migrate --noinput 

/opt/venv/bin/python manage.py createsuperuser --email $DJANGO_SUPERUSER_EMAIL --noinput || true




