from django.db import models
from django.contrib.auth.models import User

from songs.models import Song


class Preference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField(max_length=500)
    songs = models.ManyToManyField(Song, blank=True, related_name='preferences')
    some_date = models.DateField()
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return f'{self.first_name} { self.last_name } - {self.is_active}'
