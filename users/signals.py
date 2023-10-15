from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        try:
            profile = instance.profile
        except AttributeError:
            Profile.objects.create(user=instance)
        else:
            print("Профиль пользователя заполнен, поэтому не требуется автоматическое добавление")


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
