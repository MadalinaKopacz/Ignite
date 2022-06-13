from unicodedata import name
from django.db import models
from django.core.exceptions import ValidationError
from mood_quizzes.models import Question
from math import radians, sin, cos, asin, sqrt

# validators 
def validate_score(score):
    if not (0 <= score <= 10):
        raise ValidationError('Score must be between 0 and 10')


# models 
class Activity(models.Model):
    LOCATION_TYPES = [('indoor','indoor'), 
                      ('outdoor', 'outdoor'),
                      ('any', 'any')]

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200, blank=True)
    location = models.CharField(max_length=40)
    location_type = models.CharField(max_length=30, choices=LOCATION_TYPES, default='any')
    lon = models.DecimalField(max_digits=10, decimal_places=5, default=0.0)
    lat = models.DecimalField(max_digits=10, decimal_places=5, default=0.0)

    def __lt__(self, a):
        lon = radians(44.441503)
        lat = radians(26.016553)
        
        lo1 = radians(self.lon)
        lo2 = radians(a.lon)
        la1 = radians(self.lat)
        la2 = radians(a.lat)

        a = sin((lon - lo1) / 2)**2 + cos(la1) * cos(lat) * sin((lon - lo1) / 2) ** 2
        c = 2 * asin(sqrt(a))
        # Radius of earth in kilometers. Use 3956 for miles
        r = 6371
        d1 = c * r

        a = sin((lon - lo2) / 2)**2 + cos(la2) * cos(lat) * sin((lon - lo2) / 2)**2
        c = 2 * asin(sqrt(a))
        d2 = c * r

        return d1 < d2


    
    def __str__(self):
        return u'{0}'.format(self.name + ' ' + self.description + ' ' + self.location)


class Weather(models.Model):
    WEATHER_TYPES = [('sunny', 'sunny'),
                     ('cloudy', 'cloudy'), 
                     ('windy', 'windy'), 
                     ('rainy', 'rainy'),
                     ('snowy', 'snowy'),
                     ('any', 'any')]
    type = models.CharField(max_length=20, choices=WEATHER_TYPES, default='any')
    activity_id = models.ForeignKey(Activity, on_delete=models.CASCADE)


class ActivityScore(models.Model):
    type = models.CharField(max_length=40, choices=Question.TYPES, default='')
    score = models.IntegerField(validators=[validate_score])
    activity_id = models.ForeignKey(Activity, on_delete=models.CASCADE)