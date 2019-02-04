from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserExtra


# when the User is saved, the signal 'post_save' is sent
@receiver(post_save, sender=User)
def create_userextra(sender, instance, created, **kwargs):
    if created:
        UserExtra.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_userextra(sender, instance, **kwargs):
    instance.userextra.save()