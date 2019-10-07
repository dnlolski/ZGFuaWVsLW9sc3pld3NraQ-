# Api Fetcher

Hi,

Due to flu I got recently I wasn't ably to properly prepare for golang implentation. 
So I decided to stick with Python. Of course I tried to do exercise using Go but I few days I got left didn't really
allow me to properly implement the idea.

What I used:
- Python 3.6.8
- Django Rest Framework
- Redis on docker
- Celery worker and beater for task scheduling and async execution
- As db I didn't prepare anything fancy - simple built-in sqlite3.

What can be done more:
TESTS! I didn't have time to write them, unfortunately.
Also I could try to dockerize whole env. 
If I can be honest, this app is a product of one day of work. I hope I got it right at least to some extent.


Some notes for deployment on localhost.
1. clean env with Python 3.6.8
2. pip install -r requirements.txt
3. docker run --name redis-api-fetcher -d redis 
4. celery -A rest_api_fetcher worker -l info
5. celery -A rest_api_fetcher beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
6. ./manage.py runserver 8080

Thank you for this opportunity. Was fun to write this small assignment.

Regards,
Daniel
