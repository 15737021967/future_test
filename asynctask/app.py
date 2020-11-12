import pathlib
from celery import Celery
from asynctask.task import ContextTask
from asynctask.loaders import TaskDirsLoader, AsyncTaskLoader

base_dir = pathlib.Path(__name__).parent
task_dirs_loader = [TaskDirsLoader(base_dir, 'tasks')]

task_dir = AsyncTaskLoader(
    task_dirs_loader, base_dir.parent.parent
).generate_load_path()

celery_app = Celery(__name__, task_cls=ContextTask, include=task_dir)
celery_app.config_from_object('asynctask.celeryconfig')
