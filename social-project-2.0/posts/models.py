from django.db import models
from django.contrib.auth.models import User

from profiles import models as profile_models


class Post(models.Model):
    picture = models.ImageField(upload_to='posts/pictures/', blank=True)
    body = models.TextField()
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    author = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'({self.id}) {self.body[:20]} - Created at: {self.created_at}'

    @property
    def total_likes(self):
        return self.likes.count()

    @property
    def picture_url(self):
        if self.picture:
            print(self.picture.url)
        return self.picture.url if self.picture else None

    def get_likes(self):
        return self.likes.all()

    def to_json(self):
        return {
            'id': self.id,
            'picture': self.picture.url if self.picture else None,
            'body': self.body,
            'likes': self.total_likes,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }


