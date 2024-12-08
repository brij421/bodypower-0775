"""
This is the entry point for the Django application.
It provides a command-line interface to interact with the project.
"""

import os
import sys
from django.core.management import execute_from_command_line

def main():
    """
    Executes the command-line utility for administrative tasks.
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Gymnasium.settings')
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()