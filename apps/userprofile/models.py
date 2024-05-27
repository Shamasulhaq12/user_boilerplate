from django.db import models
from apps.core.models import User
from coresite.mixin import AbstractTimeStampModel


# Create your models here.


class UserProfile(AbstractTimeStampModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    city = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    zip_code = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    is_online = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name
