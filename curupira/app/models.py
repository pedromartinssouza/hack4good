"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Localization(models.Model):
    lat = models.IntegerField()
    longit = models.IntegerField()
    name = models.CharField(max_length = 100)
    monitoring = models.BooleanField()


class WeatherData(models.Model):
    umidity = models.FloatField()
    temperature = models.FloatField()
    temperatureMetric = models.CharField(max_length = 1)
    atmosphericPressure = models.FloatField()
    wind = models.FloatField()
    localization_id = models.IntegerField()
    timeStamp = models.DateTimeField()

class Event(models.Model):
    eventType = models.CharField(max_length = 30)
    startDate = models.DateField()
    endDate = models.DateField()

class WeatherPerEvent(models.Model):
    eventId = models.ForeignKey(
        'Event',
        on_delete = models.CASCADE
    )
    weatherId = models.ForeignKey(
        'WeatherData',
        on_delete = models.CASCADE
    )