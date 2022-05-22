

from django.db import models
from django.core.validators import FileExtensionValidator

from profiles.models import Profile


class Post(models.Model):
    content = models.TextField()
    image = models.ImageField(
        upload_to='posts/images',
        blank=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])
        ],
    )
    liked = models.ManyToManyField(
        Profile,
        blank=True,
        related_name='liked_posts',
    )
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')

    def __str__(self) -> str:
        return f'{self.content[:20]} - {self.author}'

    def num_of_likes(self) -> int:
        return self.liked.count()

    def num_of_comments(self) -> int:
        return self.comments.count()

    def get_comments(self):
        return self.comments.all()

    class Meta:
        ordering = ['-created',]


class Comment(models.Model):
    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='comments',
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    body = models.TextField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{str(self.body[:20])} - {str(self.user)}'


class Like(models.Model):

    class LikeValues(models.TextChoices):
        LIKE = 'LIKE'
        DISLIKE = 'DISLIKE'

    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='likes',
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='likes',
    )

    value = models.CharField(
        choices=LikeValues.choices,
        default=LikeValues.LIKE,
        max_length=10,

    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.user}-{self.post}-{self.value}'