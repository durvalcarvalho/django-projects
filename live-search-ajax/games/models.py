from django.db import models
from django.urls import reverse


class Game(models.Model):
    name = models.CharField(max_length=200)
    studio = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'studio': self.studio,
            'image': self.image.url,
            'url': reverse('games:game_detail', args=[self.id])
        }