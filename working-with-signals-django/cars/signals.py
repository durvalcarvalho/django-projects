from uuid import uuid4

from django.db.models.signals import pre_save
from django.dispatch import receiver

from cars.models import Car


@receiver(pre_save, sender=Car)
def pre_save_create_code(sender, instance, *args, **kwargs):
    if not instance.code:
        instance.code = uuid4().hex[:10]

