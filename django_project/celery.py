from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from kombu import Queue

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

app = Celery('django_project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.task_default_queue = 'default'

# Формируем три очереди
app.conf.task_queues = (
    Queue('return_exception', routing_key='task.tasks.return_exception'),
    Queue('return_status', routing_key='task.tasks.return_status'),
    Queue('test_func', routing_key='task.tasks.test_func'),
)
task_default_exchange = 'tasks'
task_default_exchange_type = 'topic'
task_default_routing_key = 'task.return_exception'

task_routes = {
        'task.tasks.return_exception': {
            'queue': 'return_exception',
            'routing_key': 'return_exception.import',
        },
        'task.tasks.return_status': {
            'queue': 'return_status',
            'routing_key': 'return_status.import',
        },
        'task.tasks.test_func': {
            'queue': 'test_func',
            'routing_key': 'test_func.import',
        },
}

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))