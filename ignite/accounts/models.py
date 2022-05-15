from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    friends = models.ManyToManyField("User", blank=True)
    profile_picture = models.ImageField(upload_to='uploads/')

