from django.db import models

# Create your models here.
class Tempo(models.Model):
    temp = models.CharField(max_length=255)
    feels_like = models.CharField(max_length=255)
    temp_min = models.CharField(max_length=255)
    temp_max = models.CharField(max_length=255)
    pressure = models.CharField(max_length=255)
    humidity = models.CharField(max_length=255)
  
