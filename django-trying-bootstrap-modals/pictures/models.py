from django.db import models


class Picture(models.Model):
    image = models.ImageField(upload_to='images/')
    info = models.CharField(max_length=200)

    def __str__(self):
        return str(self.pk)
