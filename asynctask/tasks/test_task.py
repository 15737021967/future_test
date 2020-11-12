from asynctask.app import celery_app


@celery_app.task()
def add(a, b):
    return a+b

