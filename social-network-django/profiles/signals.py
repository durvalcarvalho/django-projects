from django.db.models.signals import post_save, pre_delete
from django.contrib.auth import get_user_model
from django.dispatch import receiver

from profiles.models import Profile, Relationship

@receiver(post_save, sender=get_user_model())
def post_save_create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Relationship)
def post_save_add_to_friends(sender, instance, created, **kwargs):
    if instance.status == Relationship.StatusChoices.ACCEPTED:
        sender_profile = instance.sender
        receiver_profile = instance.receiver

        sender_profile.friends.add(receiver_profile.user)
        receiver_profile.friends.add(sender_profile.user)

        sender_profile.save()
        receiver_profile.save()


@receiver(pre_delete, sender=Relationship)
def pre_delete_remove_from_friends(sender, instance, **kwargs):
    sender = instance.sender
    receiver = instance.receiver

    sender.friends.remove(receiver.user)
    receiver.friends.remove(sender.user)

    sender.save()
    receiver.save()

