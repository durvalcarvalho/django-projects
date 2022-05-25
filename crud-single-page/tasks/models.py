from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks',
    )
    name = models.CharField(max_length=200)
    percentage_completed = models.IntegerField(default=0)

    def __str__(self):
        perc_comp = self.percentage_completed
        perc_comp = f'{perc_comp}%'
        return f'Task(name={self.name}, percentage_completed={perc_comp})'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'percentage_completed': f'{self.percentage_completed:02d}%',
        }
