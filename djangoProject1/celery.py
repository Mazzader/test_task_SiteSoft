import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject1.settings')

app = Celery('habr_scraper')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'woolworth': {
        'task': 'async_scrape_habr.tasks.scrap_posts_from_hab',
        'schedule': crontab(minute='*/10')
    }
}
app.conf.timezone = 'UTC'