from django.db import models
from django.contrib.auth.models import User
from profiles.utils import generate_ref_code


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    code = models.CharField(max_length=12, blank=True)

    recommended_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='recommendations',
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.code}'

    def get_recommended_profiles(self):
        return Profile.objects.filter(recommended_by=self.user)

    def save(self, *args, **kwargs):
        if self.code == '':
            self.code = generate_ref_code()

        super().save(*args, **kwargs)