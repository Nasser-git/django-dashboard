from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import FlightDelay

# Register your models here.

@admin.register(FlightDelay)
class FlightDelayAdmin(ImportExportActionModelAdmin):
    list_display = ('CARRIER_NAME', 'DEPARTING_AIRPORT', 'PLANE_AGE')