from django.db import models


class Question(models.Model):
    TYPES = [# de adaugat tipuri de scor
        ]
    title = models.CharField(max_length=50, blank=True)
    text = models.CharField(max_length=300)
    type = models.IntegerField(choices=[("Social", 1), 
                                        ("Physical", 2),
                                        ("Money", 3)])
