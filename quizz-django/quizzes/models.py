import random

from django.db import models


class Quiz(models.Model):
    class Meta:
        verbose_name_plural = 'Quizzes'

    class QuizDifficulty(models.TextChoices):
        EASY = 'easy', 'Easy'
        MEDIUM = 'medium', 'Medium'
        HARD = 'hard', 'Hard'

    name = models.CharField(max_length=256)
    topic = models.CharField(max_length=256)

    number_of_questions = models.PositiveIntegerField(
        default=3,
        help_text='Number of questions to be asked in the quiz.'
    )

    duration = models.IntegerField(
        help_text='Duration in minutes',
    )

    required_score = models.IntegerField(
        help_text='Required score to pass the quiz (percetage %)',
    )

    difficulty = models.CharField(
        choices=QuizDifficulty.choices,
        max_length=6,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.topic}'

    def get_questions(self):
        question = self.questions.all().order_by('?')
        return question[:self.number_of_questions]
