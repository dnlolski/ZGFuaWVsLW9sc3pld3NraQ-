# REST API fetcher

App is awaiting input from api. When received is starting to pull data from httbin site every given interval of received value from API.

Methods examples:



What I used:
- Python 3.6.8
- Django Rest Framework
- Redis on docker
- Celery worker and beater for task scheduling and async execution
- As db I didn't prepare anything fancy - simple built-in sqlite3.

What can be done more:
TESTS! I didn't have time to write them, unfortunately.
Also I could try to dockerize whole env. 
If I can be honest, this app is a product of one day of work. Good fun


Some notes for deployment on localhost.
1. clean env with Python 3.6.8
2. pip install -r requirements.txt
3. docker run --name redis-api-fetcher -d redis 
4. ./manage.py runserver 8080
5. celery -A rest_api_fetcher worker -l info
6. celery -A rest_api_fetcher beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
7. For cUrl testing. DRF requires content-type specified. So just add another switch to command, like so
-H "Content-Type:application/json"
