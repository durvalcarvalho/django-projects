from django.db import models
from django.contrib.auth.models import User


class MessageManager(models.Manager):
    def last_10_messages(self, **kwargs):
        # Filter with kwargs arguments and return the last 10 messages
        return self.filter(**kwargs)[:10]

class Message(models.Model):
    author = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    objects = MessageManager()

    def __str__(self):
        return f'{self.author.username}: {self.content}'

    def to_json(self):
        return {
            'id': self.id,
            'author': self.author.username,
            'content': self.content,
            # 'created_at': self.created_at.strftime('%b %d %Y, %H:%M:%S')
            'created_at': self.created_at.isoformat()
        }