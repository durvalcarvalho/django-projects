from django.db import models
from django.contrib.auth import get_user_model
from model_utils.models import TimeStampedModel

from repository.utils import generate_hash


class Repository(TimeStampedModel):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    star = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Repository'
        verbose_name_plural = 'Repositories'

    def __str__(self) -> str:
        return self.name


class Commit(TimeStampedModel):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.DO_NOTHING,
        related_name='commits',
    )

    repository = models.ForeignKey(
        Repository,
        on_delete=models.CASCADE,
        related_name='commits',
    )

    code = models.TextField()

    hash_value = models.CharField(max_length=40, default=generate_hash)

    def __str__(self) -> str:
        return f'commit {self.hash_value}'
