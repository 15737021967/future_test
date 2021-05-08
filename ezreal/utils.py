from ezreal.common.utils import redis_client
from redis.lock import LockError


class lock_by_key:
    def __init__(self, key, timeout=60, blocking=True, blocking_timeout=5):
        """
        :param timeout:如果 timeout秒 后程序都没结束完，则释放锁
        :param blocking:如果第二个冲突的程序尝试运行，是否等待/直接报错
        :param blocking_timeout: 如果blocking is True，那么等待多少秒
        :return:
        """
        self.lock = redis_client.lock(str(key), timeout=timeout, blocking_timeout=blocking_timeout)
        self.timeout = timeout
        self.blocking = blocking
        self.blocking_timeout = blocking_timeout

    def __enter__(self):
        if not self.lock.acquire(blocking=self.blocking):  # 如果已有这个key，返回False
            raise LockError('time out ')

    def __exit__(self, exc_type, exc_value, exc_track_back):
        self.lock.release()
