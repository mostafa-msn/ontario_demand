import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ontario.settings')

app = Celery(
    'ontario',
    broker=settings.REDIS_CONNECTION_URI,
    backend=settings.REDIS_CONNECTION_URI,
)

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {

    'fetch-ontario-demand': {
        'task': 'demand.tasks.fetch_ontario_csv',
        'schedule': crontab(minute='*/2'),
        'args': tuple()
    },

}
app.conf.timezone = settings.TIME_ZONE
