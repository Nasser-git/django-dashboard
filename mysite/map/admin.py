from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import UserLocation

# Register your models here.

# admin.site.register(UserLocation)

@admin.register(UserLocation)
class UserLocationAdmin(ImportExportActionModelAdmin):
    list_display = ('User', 'Location')