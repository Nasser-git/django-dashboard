from django.db import models

# Create your models here.

class UserLocation(models.Model):
    User = models.CharField(max_length=15)
    Location = models.CharField(max_length=15)