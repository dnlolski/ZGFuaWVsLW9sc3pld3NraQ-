import requests

from celery.utils.log import get_task_logger

from rest_api_fetcher.celery import app
from .models import History

logger = get_task_logger(__name__)


@app.task
def save_data_from_url(url, item_id):
    payload = None
    duration = 5
    try:
        response = requests.get(url, timeout=duration)
        payload = response.text
        duration = response.elapsed.total_seconds()
    except requests.exceptions.Timeout:
        pass
    finally:
        history = History(item_id=item_id, response=payload, duration=duration)
        history.save()
