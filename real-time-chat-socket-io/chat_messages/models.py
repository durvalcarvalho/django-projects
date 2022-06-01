from django.db import models
from django.contrib.auth.models import User

from chats.models import Chat


class ChatMessage(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    message = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.chat.room_name} - {self.sender} - {self.message}'

    class Meta:
        ordering = ['created_at']