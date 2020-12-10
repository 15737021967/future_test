import pickle
from rpc.proxy import RPCProxy
from multiprocessing.connection import Client


if __name__ == '__main__':
    c = Client(("localhost", 17000), authkey=b"jiale.tan")
    proxy = RPCProxy(c)
    print(proxy.add(2, 3))
    import ipdb;ipdb.set_trace()
