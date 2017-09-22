# The test task
My first django project.

Base requirements:
* Python 3.6
* Django 1.11
* Celery 4.1
* PostgreSQL 9.2.23
* RabbitMQ
* Celery-flower

## Installing requirements
    $ pip install -r requirements.txt
## Starting RabbitMQ
    $ rabbitmq-server
## Starting Flower
    $ flower -A django_project --port=5555
## Startpage  
    http://127.0.0.1:8000/task/add/
## Starting the workers
### First worker
    $ celery worker -A django_project --concurrency=4 -l info -Q return_exception -P eventlet
### Second worker
    $ celery worker -A django_project --concurrency=4 -l info -Q return_status -P eventlet
### Third worker
    $ celery worker -A django_project --concurrency=4 -l info -Q test_func -P eventlet    

