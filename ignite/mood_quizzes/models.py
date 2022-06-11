from django.db import models


class Question(models.Model):
    TYPES = [(1,"Social"), (2, "Physical"),(3,"Money")]
    title = models.CharField(max_length=50, blank=True)
    text = models.CharField(max_length=300)
    qtype = models.IntegerField(choices = TYPES)