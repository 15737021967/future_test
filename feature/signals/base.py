from typing import List, Tuple


class Signal:

    def __init__(self):
        self.receivers: List[Tuple[Tuple[int, int], callable]] = []

    def send(self, sender, **kwargs):
        return [
            (receiver, receiver(signal=self, sender=sender, **kwargs))
            for receiver in self.live_receivers(sender=sender)
        ]

    def connect(self, receiver: callable, sender=None):
        lookup_key: Tuple[int, int] = (id(receiver), id(sender))

        self.receivers.append((lookup_key, receiver))

    def disconnect(self, receiver: callable, sender=None):
        lookup_key: Tuple[int, int] = (id(receiver), id(sender))

        self.receivers.remove((lookup_key, receiver))

    def live_receivers(self, sender) -> List[callable]:
        receivers: List[callable] = []
        sender_key = id(sender)
        for (receiver_id, sender_id), receiver in self.receivers:
            if sender_key == sender_id:
                receivers.append(receiver)
        return receivers


def subscribe(signal, **kwargs):

    def _decorator(func):
        if isinstance(signal, (list, tuple)):
            for s in signal:
                s.connect(func, **kwargs)
        else:
            signal.connect(func, **kwargs)
        return func
    return _decorator
