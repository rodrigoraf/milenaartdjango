import os
import sys

# Add your project directory to the sys.path
project_home = '/home/SEU_USERNAME/milenaartdjango'  # Substitua SEU_USERNAME pelo seu username no PythonAnywhere
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set environment variable to tell django where your settings.py is
os.environ['DJANGO_SETTINGS_MODULE'] = 'milenaart.settings'

# Serve django via WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
