import os
import dotenv

dotenv.load_dotenv(verbose=True)


broker_url = os.environ.get("CELERY_BROKER_URL")
result_backend = os.environ.get("CELERY_RESULT_BACKEND")

"""
    accept_content: 允许收到的消息的类型。如果不在列表中就抛出错误
    task_annotations：可以用来重写任意任务的属性。
     - eg. task_annotations = {'tasks.add': {'rate_limit': '10/s'}} 更改 tasks.add 任务的 rate_limit 属性
    task_serializer: task任务使用的序列化方式
    task_ignore_result：True不存储任务的返回值
    task_acks_late：True任务在执行完成后再确认
    task_reject_on_worker_lost：True当处理任务的工作单元异常退出或者收到信号而退出时工作单元将会将任务重新放回队列
    task_send_sent_event：如果启用，对于每个任务都将有一个 task-sent 事件被发送，因此任务在被消费前就能被追踪
    task_time_limit: 任务的时间限制，以秒为单位。如果这个时间限制被超过，处理任务的工作单元进程将会被杀死并使用一个新的替代。
    worker_prefetch_multiplier: 每个worker取出的消息数，默认为4
    worker_max_tasks_per_child：一个工作单元进程在被一个新的进程替代之前可以执行的最大任务数
    redis_socket_connect_timeout：从存储后端连接到Redis服务器的连接的Socket超时时间
    redis_socket_timeout：redis操作的超时时间
"""

timezone = "Asia/Shanghai"
accept_content = [
    "pickle",
    "application/json",
    "json",
]

task_serializer = 'pickle'
task_ignore_result = True
task_acks_late = True
task_reject_on_worker_lost = True
task_send_sent_event = True
task_time_limit = int(os.environ.get("CELERY_TASK_TIME_LIMIT", 60))

worker_prefetch_multiplier = 1
worker_max_tasks_per_child = 500
redis_socket_connect_timeout = 10
redis_socket_timeout = 10

