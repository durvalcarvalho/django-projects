from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver

from orders.models import Order
from sales.models import Sales


@receiver(m2m_changed, sender=Order.cars.through)
def m2m_changed_update_total(sender, instance, action, **kwargs):
    if action in ('post_add', 'post_remove'):
        instance.total = instance.cars.count()
        instance.total_price = sum(car.price for car in instance.cars.all())
        instance.save()


@receiver(post_save, sender=Order)
def post_save_create_or_update_sales(sender, instance, created, **kwargs):
    sale, _ = Sales.objects.get_or_create(order=instance)

    sale.amount = instance.total_price
    sale.save()
