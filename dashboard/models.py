from django.db import models


class Data(models.Model):
    country = models.CharField(max_length=100)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    population = models.PositiveIntegerField()

    def __str__(self):
        return self.country
