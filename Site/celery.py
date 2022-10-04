import os

from django.conf import settings

from celery import Celery

from django_celery_results.apps import CeleryResultConfig

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Site.settings')


app = Celery('Site')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

CeleryResultConfig.verbose_name = "Результаты Celery"