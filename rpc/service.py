import pickle
import logging
from multiprocessing.connection import Listener
from threading import Thread

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


class RPCHandler:
    def __init__(self):
        self._functions = {}

    def register_function(self, func):
        self._functions[func.__name__] = func

    def handle_connection(self, connection):

        try:
            while True:
                func_name, args, kwargs = pickle.loads(connection.recv())
                try:
                    r = self._functions[func_name](*args, **kwargs)
                    connection.send(pickle.dumps(r))
                except Exception as e:
                    connection.send(pickle.dumps(e))
        except (EOFError, KeyboardInterrupt):
            connection.close()
            logger.info(f"断开连接{connection}")


def rpc_server(handler, address, authkey):
    sock = Listener(address=address,  authkey=authkey)
    while True:
        client = sock.accept()
        logger.info(f"建立连接{client}")
        t = Thread(target=handler.handle_connection, args=(client, ))
        t.daemon = True
        t.start()


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


if __name__ == '__main__':

    handler = RPCHandler()
    handler.register_function(add)
    handler.register_function(sub)
    rpc_server(handler=handler, address=("localhost", 17000), authkey=b"jiale.tan")
