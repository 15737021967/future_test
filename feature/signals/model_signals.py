from feature.signals.base import Signal


class ModelSignal(Signal):

    pass


pre_init = ModelSignal()
post_init = ModelSignal()

pre_save = ModelSignal()
post_save = ModelSignal()

pre_delete = ModelSignal()
post_delete = ModelSignal()


from django.db.models.signals import pre_init
from django.core.signals import request_finished
from django.test.signals import template_rendered
from django.db.models.base import Model
