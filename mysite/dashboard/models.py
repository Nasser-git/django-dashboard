from django.db import models

class FlightDelay(models.Model):
    MONTH = models.CharField(max_length=15)
    DAY_OF_WEEK = models.CharField(max_length=15)
    DEP_DEL15 = models.CharField(max_length=2)
    DEP_TIME_BLK = models.CharField(max_length=15)
    DISTANCE_GROUP = models.CharField(max_length=15)
    SEGMENT_NUMBER = models.CharField(max_length=15)
    CONCURRENT_FLIGHTS = models.CharField(max_length=15)
    NUMBER_OF_SEATS = models.CharField(max_length=15)
    CARRIER_NAME = models.CharField(max_length=100)
    AIRPORT_FLIGHTS_MONTH = models.CharField(max_length=15)
    AIRLINE_FLIGHTS_MONTH = models.CharField(max_length=15)
    AIRLINE_AIRPORT_FLIGHTS_MONTH = models.CharField(max_length=15)
    AVG_MONTHLY_PASS_AIRPORT = models.CharField(max_length=15)
    AVG_MONTHLY_PASS_AIRLINE = models.CharField(max_length=15)
    FLT_ATTENDANTS_PER_PASS = models.CharField(max_length=50)
    GROUND_SERV_PER_PASS = models.CharField(max_length=50)
    PLANE_AGE = models.CharField(max_length=15)
    DEPARTING_AIRPORT = models.CharField(max_length=100)
    LATITUDE = models.CharField(max_length=50)
    LONGITUDE = models.CharField(max_length=50)
    PREVIOUS_AIRPORT = models.CharField(max_length=100)
    PRCP = models.CharField(max_length=50)
    SNOW = models.CharField(max_length=50)
    SNWD = models.CharField(max_length=50)
    TMAX = models.CharField(max_length=50)
    AWND = models.CharField(max_length=50)


