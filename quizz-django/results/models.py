from django.db import models
from django.contrib.auth.models import User

from quizzes.models import Quiz



class Result(models.Model):
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name='results',
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='results',
    )

    score = models.IntegerField()


    def __str__(self):
        return f'{self.user.username} - {self.quiz.name} - {self.score}%'


