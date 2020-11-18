from blog.signals.base import Signal


class ModelSignal(Signal):

    pass


pre_init = ModelSignal()
post_init = ModelSignal()

pre_save = ModelSignal()
post_save = ModelSignal()

pre_delete = ModelSignal()
post_delete = ModelSignal()
