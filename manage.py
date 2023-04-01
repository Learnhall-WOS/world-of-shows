#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wos.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Set default port to 8000
    # default_port = '9000'
    # Add default port as argument to execute_from_command_line
    # execute_from_command_line(['manage.py', 'runserver', str(default_port)])

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
