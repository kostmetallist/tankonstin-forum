from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserExtra
from os import path
from shutil import rmtree


# when the User is saved, the signal 'post_save' is sent
@receiver(post_save, sender=User)
def create_userextra(sender, instance, created, **kwargs):
    if created:
        UserExtra.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_userextra(sender, instance, **kwargs):
    instance.userextra.save()

# When the User is deleted or UserExtra is deleted (btw, first
# implicates second because of on_delete=CASCADE), all the files
# related to that user must be cleaned out. By the convention, 
# that files are placed in media_files/user_<user_id>/
@receiver(post_delete, sender=UserExtra)
def delete_user_files(sender, instance, *args, **kwargs):

    file_dir = 'media_files/user_' + str(instance.user.id)

    if path.isdir(file_dir):
        rmtree(file_dir)