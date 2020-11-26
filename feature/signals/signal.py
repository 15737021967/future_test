from feature.signals.base import subscribe
from feature.signals.model_signals import pre_init, post_init
from feature.signals.test_model import TestModel


@subscribe(pre_init, sender=TestModel)
def test_pre_init(sender, **kwargs):
    print("-------pre_init_______")
    print(sender)
    print(kwargs)
    print("-------end_pre_init_______")


@subscribe(post_init, sender=TestModel)
def test_post_init(sender, **kwargs):
    print("-------post_init_______")
    print(sender)
    print(kwargs)
    print("-------end_post_init_______")


