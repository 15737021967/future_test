import celery
from abc import ABC
from ezreal import app


class ContextTask(celery.Task, ABC):
    def __call__(self, *args, **kwargs):
        with app.app_context():
            return self.run(*args, **kwargs)

    def on_retry(self, exc, task_id, args, kwargs, einfo):
        super(ContextTask, self).on_retry(exc, task_id, args, kwargs, einfo)

    def on_success(self, retval, task_id, args, kwargs):
        super(ContextTask, self).on_success(retval, task_id, args, kwargs)

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        super(ContextTask, self).on_failure(exc, task_id, args, kwargs, einfo)



