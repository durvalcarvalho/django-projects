from django.db import models

from django.contrib.auth import get_user_model


User = get_user_model()


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=256, blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        status = 'Completed' if self.completed else 'Incomplete'
        return f'[{self.user.username}] - {self.title} - {status}'

    class Meta:
        ordering = ['completed']


    def get_task_icon_css(self):
        return 'task-completed-icon' if self.completed else 'task-incomplete-icon'