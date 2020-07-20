from django.db import models
from django.contrib.auth.models import AbstractUser




class UserDetails(AbstractUser):
    roles = models.CharField(max_length=50)


class UserAPIKey(models.Model):
    user_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    apiKey= models.CharField(max_length=20)
    createDate= models.DateTimeField(auto_now=True)


def user_directory_path(userId, clientId):
    return '{0}/{1}'.format(userId, clientId)


class UserImages(models.Model):
    user_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    client_id = models.CharField(max_length=8, blank=True)
    image = models.ImageField(upload_to= user_directory_path(user_id, client_id),  max_length=1000, null=True, blank=True)

