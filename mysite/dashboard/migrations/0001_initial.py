# Generated by Django 5.0.4 on 2024-04-16 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlightDelay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MONTH', models.IntegerField()),
                ('DAY_OF_WEEK', models.IntegerField()),
                ('DEP_DEL15', models.BinaryField()),
                ('DEP_TIME_BLK', models.CharField(max_length=15)),
                ('DISTANCE_GROUP', models.IntegerField()),
                ('SEGMENT_NUMBER', models.IntegerField()),
                ('CONCURRENT_FLIGHTS', models.IntegerField()),
                ('NUMBER_OF_SEATS', models.IntegerField()),
                ('CARRIER_NAME', models.CharField(max_length=100)),
                ('AIRPORT_FLIGHTS_MONTH', models.IntegerField()),
                ('AIRLINE_FLIGHTS_MONTH', models.IntegerField()),
                ('AIRLINE_AIRPORT_FLIGHTS_MONTH', models.IntegerField()),
                ('AVG_MONTHLY_PASS_AIRPORT', models.IntegerField()),
                ('AVG_MONTHLY_PASS_AIRLINE', models.IntegerField()),
                ('FLT_ATTENDANTS_PER_PASS', models.FloatField()),
                ('GROUND_SERV_PER_PASS', models.FloatField()),
                ('PLANE_AGE', models.IntegerField()),
                ('DEPARTING_AIRPORT', models.CharField(max_length=100)),
                ('LATITUDE', models.FloatField()),
                ('LONGITUDE', models.FloatField()),
                ('PREVIOUS_AIRPORT', models.CharField(max_length=100)),
                ('PRCP', models.FloatField()),
                ('SNOW', models.FloatField()),
                ('SNWD', models.FloatField()),
                ('TMAX', models.FloatField()),
                ('AWND', models.FloatField()),
            ],
        ),
    ]
