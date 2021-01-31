from datetime import datetime, timedelta

import pytz
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatar', blank=True)
    age = models.PositiveSmallIntegerField(verbose_name='age', default=18)
    is_active = models.BooleanField(verbose_name='active', default=True)

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=(datetime.now() + timedelta(hours=48)))

    def is_activation_key_expired(self):
        if datetime.now() > self.activation_key_expires:
            #print(datetime.now(pytz.timezone(settings.TIME_ZONE)))
            return True
        else:
            #print(datetime.now(pytz.timezone(settings.TIME_ZONE)))
            return False

class ShopUserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'M'),
        (FEMALE, 'F')
    )
    user = models.OneToOneField(ShopUser, unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    tagline = models.CharField(max_length=128, blank=True, verbose_name='tagline')
    about_me = models.TextField(blank=True, verbose_name='about me')
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, blank=True, verbose_name='gender')

    @receiver(post_save, sender=ShopUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            ShopUserProfile.objects.create(user=instance)

    @receiver(post_save, sender=ShopUser)
    def save_user_profile(sender, instance, **kwargs):
        instance.shopuserprofile.save()


