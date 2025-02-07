from __future__ import absolute_import, unicode_literals
import os
from celery import Celery, signals
from django.conf import settings


# Set the default Django settings module for the "celery" program
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "time_swap.settings")

app = Celery("time_swap")

# Using a string here means the worker does not have to serialize
# the configuration object to child process
app.config_from_object("django.conf.settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()