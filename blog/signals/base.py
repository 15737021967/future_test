from typing import List


class Signal:

    def __init__(self):
        self.receivers: List[callable] = []

    def send(self, sender, **kwargs):
        return [
            (receiver, receiver(signal=self, sender=sender, **kwargs))
            for receiver in self.receivers
        ]

    def connect(self, receiver, sender=None):

        self.receivers.append(receiver)

    def disconnect(self, receiver):

        self.receivers.remove(receiver)


def receivers(signal, **kwargs):

    def _decorator(func):
        if isinstance(signal, (list, tuple)):
            for s in signal:
                s.connect(func, **kwargs)
        else:
            signal.connect(func, **kwargs)
        return func
    return _decorator
