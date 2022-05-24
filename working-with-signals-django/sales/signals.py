from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver

from sales.models import Sales
from orders.models import Order


@receiver(pre_delete, sender=Sales)
def pre_delete_set_order_to_non_active(sender, instance, **kwargs):
    instance.order.is_active = False
    instance.order.save()

@receiver(pre_save, sender=Sales)
def pre_save_fetch_order_amount(sender, instance, **kwargs):
    instance.amount = instance.order.total_price