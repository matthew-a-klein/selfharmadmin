#!/bin/bash

# Default to port 8000 if no PORT environment variable is set
APP_PORT=${PORT:-8000}


# Navigate to the application directory
cd /app/

# Activate the virtual environment
source /opt/venv/bin/activate



# Start the Gunicorn server
/opt/venv/bin/gunicorn --worker-tmp-dir /dev/shm selfharmadmin.wsgi:application --bind "0.0.0.0:${APP_PORT}"
