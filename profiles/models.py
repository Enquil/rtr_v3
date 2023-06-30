from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

'''
    UserProfile and reciever
    handling sourced from CodeInstitute
'''


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_update_user_profile(sender, instance, created, **kwargs):

    if created:
        UserProfile.objects.create(user=instance)
    # Existing users, just save the profile
    instance.userprofile.save()
