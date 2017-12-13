from django.db.models.signals import pre_save
from django.core.signals import request_finished
from django.dispatch import receiver
from gym.models import Set

@receiver(request_finished)
def handle_request_start(sender, **kwargs):
    print("Request finished!")

@receiver(pre_save, sender=Set)
def handle_pre_save(sender, **kwargs):
    print("Pre save!")
