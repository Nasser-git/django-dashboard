from django.shortcuts import render
from .models import FlightDelay
from .resources import FlightDelayResource
from django.contrib import messages
from tablib import Dataset
import csv,io
from django import forms

# Create your views here.

def dashboard_page(request):
    if request.method == 'POST':
        if 'myfile' in request.FILES:
            new_flightdelay = request.FILES["myfile"]
            if not new_flightdelay.name.endswith('csv'):
                messages.error(request, 'Please Upload the CSV File only')
            else:
                messages.info(request, 'File successfully uploaded')
                data_set = new_flightdelay.read().decode('UTF-8')
                io_string = io.StringIO(data_set)
                next(io_string)
                for column in csv.reader(io_string, delimiter=',', quotechar="|"):
                    FlightDelay.objects.update_or_create(
                        MONTH=column[0],
                        DAY_OF_WEEK=column[1],
                        DEP_DEL15=column[2],
                        DEP_TIME_BLK=column[3],
                        DISTANCE_GROUP=column[4],
                        SEGMENT_NUMBER=column[5],
                        CONCURRENT_FLIGHTS=column[6],
                        NUMBER_OF_SEATS=column[7],
                        CARRIER_NAME=column[8],
                        AIRPORT_FLIGHTS_MONTH=column[9],
                        AIRLINE_FLIGHTS_MONTH=column[10],
                        AIRLINE_AIRPORT_FLIGHTS_MONTH=column[11],
                        AVG_MONTHLY_PASS_AIRPORT=column[12],
                        AVG_MONTHLY_PASS_AIRLINE=column[13],
                        FLT_ATTENDANTS_PER_PASS=column[14],
                        GROUND_SERV_PER_PASS=column[15],
                        PLANE_AGE=column[16],
                        DEPARTING_AIRPORT=column[17],
                        LATITUDE=column[18],
                        LONGITUDE=column[19],
                        PREVIOUS_AIRPORT=column[20],
                        PRCP=column[21],
                        SNOW=column[22],
                        SNWD=column[23],
                        TMAX=column[24],
                        AWND=column[25]
                    )
    data = FlightDelay.objects.all()
    return render(request, 'dashboard.html', {"flights": data})