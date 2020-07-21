from django.db import models
from django.contrib.auth.models import AbstractUser




class UserDetails(AbstractUser):
    roles = models.CharField(max_length=50)


class UserAPIKey(models.Model):
    user_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    apiKey= models.CharField(max_length=20)
    createDate= models.DateTimeField(auto_now=True)


def user_directory_path(instance, filename):
    return '{0}/{1}/{2}'.format(instance.user_id.id, instance.client_id, filename)


class UserImages(models.Model):
    user_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    client_id = models.CharField(max_length=8, blank=True)
    image = models.ImageField(upload_to=user_directory_path,  max_length=1000, null=True, blank=True)

