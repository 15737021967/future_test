import pickle


class RPCProxy:

    def __init__(self, connection):
        self._connection = connection

    def __getattr__(self, item):
        def do_rpc(*args, **kwargs):
            self._connection.send(pickle.dumps((item, args, kwargs)))
            result = pickle.loads(self._connection.recv())
            if isinstance(result, Exception):
                raise result
            return result
        return do_rpc
