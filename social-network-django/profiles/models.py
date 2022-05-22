import itertools

from django.db import models
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from django.urls import reverse

from profiles.utils import get_random_code


class ProfileManager(models.Manager):
    def get_all_profiles(self, user):
        return Profile.objects.all().exclude(user=user)

    def get_all_profiles_to_invite(self, profile):
        """
        Get all profiles except the ones that are already has a pending invitation
        """
        qs = Relationship.objects.filter(
            Q(sender=profile) |
            Q(receiver=profile)
        ).values_list('sender', 'receiver')

        ids = list(itertools.chain(*list(qs)))

        return Profile.objects.exclude(id__in=ids)



class Profile(models.Model):
    objects = ProfileManager()

    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name  = models.CharField(max_length=200, blank=True, null=True)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(default='no bio...', max_length=300)

    email = models.EmailField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    avatar = models.ImageField(default='avatar.png', upload_to='avatars/')
    friends = models.ManyToManyField(get_user_model(), blank=True, related_name='friends')
    slug = models.SlugField(unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    __initial_first_name = None
    __initial_last_name = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__initial_first_name = self.first_name
        self.__initial_last_name = self.last_name

    def get_absolute_url(self):
        return reverse("profiles:profile-detail-view", kwargs={"pk": self.pk})


    def __str__(self):
        created_str = self.created.strftime('%d-%m-%Y')
        return f'{self.user.username}-{created_str}'

    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def username(self):
        return self.user.username

    def get_friends(self):
        return self.friends.all()

    def get_friends_count(self):
        return self.friends.count()

    def get_posts_count(self):
        return self.posts.count()

    def get_comments_count(self):
        return self.comments.count()

    def get_public_posts(self):
        return self.posts.all()

    def get_likes_given_count(self):
        from posts.models import Like
        qs = self.likes.filter(value=Like.LikeValues.LIKE)
        return qs.count()

    def get_invitations_received(self):
        return Relationship.objects.filter(
            receiver=self,
            status=Relationship.StatusChoices.SENT,
        )

    def get_number_of_received_invitations(self):
        return self.get_invitations_received().count()

    def get_likes_received_count(self):
        from posts.models import Like
        qs = self.posts.all()

        qs = qs.annotate(
            likes_count=models.Count(
                'likes',
                filter=models.Q(likes__value=Like.LikeValues.LIKE),
            ),
        )

        result: dict = qs.aggregate(likes_received=models.Sum('likes_count'))
        return result['likes_received']

    def save(self, *args, **kwargs):
        to_slug = self.slug

        if(
            (
                self.first_name != self.__initial_first_name or
                self.last_name != self.__initial_last_name
            ) or

            self.slug == ''
        ):
            to_slug = slugify(f'{self.first_name} {self.last_name}')

            while ex := Profile.objects.filter(slug=to_slug).exists():
                code = get_random_code()
                to_slug = slugify(f'{to_slug} {code}')

        elif self.first_name == '' and self.last_name == '':
            to_slug = str(self.user)

        self.slug = to_slug
        return super().save(*args, **kwargs)


class RelationshipManager(models.Manager):
    def invitations_received(self, receiver):
        return Relationship.objects.filter(receiver=receiver, status=Relationship.StatusChoices.SENT)




class Relationship(models.Model):

    objects = RelationshipManager()

    class StatusChoices(models.TextChoices):
        SENT = 'sent', 'Sent'
        ACCEPTED = 'accepted', 'Accepted'
        CANCELED = 'canceled', 'Canceled'

    sender = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='invitations_sent',
    )
    receiver = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='invitations_received',
    )

    status = models.CharField(max_length=8, choices=StatusChoices.choices, default=StatusChoices.SENT)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender}-{self.receiver}-{self.status}'
