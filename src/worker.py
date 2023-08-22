import os

from celery import Celery


# ----------------------------------------------------------------
# init celery obj
celery = Celery(
    'tasks',
    broker=os.environ.get('CELERY_BROKER_URL'),
    backend=os.environ.get('CELERY_RESULT_BACKEND')
)

celery.config_from_object('src.config.celery')
