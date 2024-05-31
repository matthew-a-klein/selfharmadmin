FROM python:3.10.12-slim

# Copy application code to /app directory
COPY . /app
WORKDIR /app

# Create a virtual environment and install dependencies
RUN python3 -m venv /opt/venv
RUN /opt/venv/bin/pip install pip --upgrade
RUN /opt/venv/bin/pip install -r requirements.txt



# Ensure the entrypoint script is executable
RUN chmod +x entrypoint.sh


# Define the entry point for the container
CMD ["/app/entrypoint.sh"]
