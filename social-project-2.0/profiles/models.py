from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from posts import models as post_models


class Profile(models.Model):
    user =  models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(
        upload_to='avatars/',
        default='avatars/default.png',
    )

    background = models.ImageField(
        upload_to='backgrounds/',
        default='backgrounds/default.png',
    )

    following = models.ManyToManyField(
        'self',
        related_name='followers',
        symmetrical=False,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'({self.id}) {self.user.username} - Created at: {self.created_at}'

    def to_json(self):
        following_profiles = self.get_following_profiles()
        following_profiles = [str(profile) for profile in following_profiles]

        followers_profiles = self.get_followers()
        followers_profiles = [str(profile) for profile in followers_profiles]

        return {
            'id': self.id,
            'username': self.user.username,
            'avatar': self.avatar.url,
            'background': self.background.url,
            'following': following_profiles,
            'following_count': self.get_following_count(),
            'followers': followers_profiles,
            'followers_count': self.get_followers_count(),
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }

    def get_posts(self):
        return self.posts.all()

    def get_post_count(self):
        return self.posts.count()

    def get_following_profiles(self):
        return self.following.all()

    def get_following_count(self):
        return self.following.count()

    def get_followers(self):
        return self.followers.all()

    def get_followers_count(self):
        return self.followers.count()

    def get_following_posts(self):
        following_profiles_ids = list(self.following.values_list('id', flat=True))
        following_profiles_ids.append(self.id)

        posts = post_models.Post.objects.filter(
            author_id__in=following_profiles_ids
        )

        posts = posts.order_by('-created_at')

        return posts

    def get_unfollowed_profiles(self):
        following_profiles_ids = list(self.following.values_list('id', flat=True))
        following_profiles_ids.append(self.id)
        return Profile.objects.exclude(id__in=following_profiles_ids)

