from django.db import models


class Club(models.Model):
    name = models.CharField(max_length=100)
    money = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.money}'

