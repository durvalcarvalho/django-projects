from django.db import models

from cars.models import Car


class Order(models.Model):
    name = models.CharField(max_length=100)
    cars = models.ManyToManyField(Car, related_name='orders')
    total = models.PositiveIntegerField(blank=True, null=True)
    total_price = models.PositiveIntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'Order(name={self.name}, total={self.total}, total_price={self.total_price}, is_active={self.is_active})'
