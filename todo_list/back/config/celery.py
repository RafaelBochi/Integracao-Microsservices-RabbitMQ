from __future__ import absolute_import, unicode_literals
import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_list.settings')

app = Celery('todo_list', broker='amqp://guest:guest@localhost:5672//')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.broker_connection_retry_on_startup = True

app.autodiscover_tasks()