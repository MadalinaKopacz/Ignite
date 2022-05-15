from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    friends = models.ManyToManyField("User", blank=True)
    profile_picture = models.ImageField(upload_to='uploads/')


class Friend_Request(models.Model):
    from_user = models.ForeignKey(User, related_name='from_user',
    on_delete = models.CASCADE)

    to_user = models.ForeignKey(User, related_name='to_user',
    on_delete=models.CASCADE)

    def __str__(self):
        return u'{0}'.format(self.from_user.username)
    