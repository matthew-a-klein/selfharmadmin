#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import dotenv
import pathlib





def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'selfharmadmin.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


CURRENT_DIR = pathlib.Path(__file__).resolve().parent

ENV_FILE_PATH = CURRENT_DIR / ".env"


if __name__ == '__main__':
    dotenv.read_dotenv(ENV_FILE_PATH)
    main()
