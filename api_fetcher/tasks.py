import requests

from celery.utils.log import get_task_logger

from rest_api_fetcher.celery import app
from .models import History

logger = get_task_logger(__name__)


@app.task(name="get_data_from_url")
def save_data_from_url(url, item_id):
    response = requests.get(url)
    history = History(item_id=item_id, response=response.text, duration=response.elapsed)
    history.save()
