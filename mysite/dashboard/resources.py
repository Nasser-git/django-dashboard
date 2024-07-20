from import_export import resources
from .models import FlightDelay


class FlightDelayResource(resources.ModelResource):
    class Meta:
        model = FlightDelay