from ezreal.signals.model_signals import pre_init, post_init


class TestModel:

    def __init__(self, *args, **kwargs):
        cls = self.__class__
        pre_init.send(sender=cls, args=args, kwargs=kwargs)
        for key, value in kwargs.items():
            setattr(self, key, value)
        post_init.send(sender=cls, instance=self)




