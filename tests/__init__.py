import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "tests.settings")

from django.test.utils import setup_test_environment
setup_test_environment()

# Django 1.7
import django
if hasattr(django, 'setup'):
    django.setup()
