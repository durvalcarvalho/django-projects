from django.db import models

from orders.models import Order


class Sales(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f'Sales(order={self.order.name}, amount={self.amount})'

    class Meta:
        verbose_name = 'Sales'
        verbose_name_plural = 'Sales'
