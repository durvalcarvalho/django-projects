from uuid import uuid4

from django.db import models

from buyers.models import Buyer


class Car(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(
        help_text="Price in BRL cents",
        verbose_name="Price in BRL cents"
    )
    buyer = models.ForeignKey(
        Buyer,
        on_delete=models.CASCADE,
        related_name='cars',
    )

    code = models.CharField(max_length=10, blank=True, null=True)

    # brand = models.CharField(max_length=100)
    # year = models.IntegerField()
    # color = models.CharField(max_length=100)
    # photo = models.ImageField(upload_to='cars/photos')
    # description = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Car(name={self.name}, price={self.price}, buyer={self.buyer.user.username}, code={self.code})'

    # def save(self, *args, **kwargs):
    #     if not self.code:
    #         self.code = uuid4().hex[:10]

    #     super().save(*args, **kwargs)
