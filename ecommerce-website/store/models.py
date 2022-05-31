from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from django.urls import reverse_lazy


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, related_name='customer')
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.name}'


class Product(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    price_cents = models.PositiveBigIntegerField(default=0, help_text='Price in cents')
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='images')

    def __str__(self):
        return f'{self.name} - {self.price}'

    @property
    def price(self):
        return f'BRL {self.price_cents / 100}'

    @price.setter
    def price(self, value):
        self.price_cents = value * 100

    def get_absolute_url(self, *args, **kwargs):
        return reverse_lazy('store:product-detail-view', kwargs={'pk': self.pk})

    @property
    def image_url(self, *args, **kwargs):
        if not self.image:
            return "{0}{1}".format(settings.MEDIA_URL, 'images/placeholder.png')
        return self.image.url


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.id} - {self.transaction_id}'

    @property
    def get_cart_total_value(self):
        order_items = self.orderitems.all()
        total_cents = sum(item.total_cents for item in order_items)
        return f'BRL {total_cents / 100}'

    @property
    def get_cart_items_total(self):
        order_items = self.orderitems.all()
        return sum(item.quantity for item in order_items)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True, related_name='orderitems')
    quantity = models.PositiveIntegerField(default=1, null=True, blank=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'(Order: {self.order.id}) - {self.product.name} - {self.quantity}'

    @property
    def total_cents(self):
        return self.product.price_cents * self.quantity

    @property
    def total(self):
        total_cents = self.product.price_cents * self.quantity
        return f'BRL {total_cents / 100}'

    @property
    def name(self):
        return self.product.name

    @property
    def price(self):
        return self.product.price

    @property
    def image_url(self):
        return self.product.image_url

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity,
            'total': self.total,
            'image_url': self.image_url
        }


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, related_name='shipping_addresses')
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True, related_name='shipping_addresses')
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    zip_code = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer.user.username} - {self.address} - {self.city} - {self.state} - {self.zip_code} - {self.country}'
