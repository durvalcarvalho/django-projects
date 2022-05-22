import random

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from django.utils import timezone
from repository.models import Repository, Commit


class Command(BaseCommand):
    help = "Generate commits"

    def handle(self, *args, **options):
        user = get_user_model().objects.first()

        if not user:
            raise CommandError('Create a superuser before running this command')

        now = timezone.now()
        previous_year = now - timezone.timedelta(weeks=52)

        repo, created = Repository.objects.get_or_create(
            name='The Next Facebook',
            user=user,
        )

        repo.created = previous_year
        repo.save()

        Commit.objects.filter(repository=repo).delete()

        delta = now - previous_year

        for n in range(delta.days):
            day = previous_year + timezone.timedelta(days=n)

            if random.uniform(0, 1) > 0.5:
                continue

            num_commits = random.randint(1, 10)

            for _ in range(num_commits):
                Commit.objects.create(
                    user=user,
                    repository=repo,
                    code='print("hello world")',
                    created=day,
                )

