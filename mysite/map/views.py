from django.shortcuts import render
import folium
import geocoder
from .models import UserLocation
# Create your views here.


def map(request):
    m = folium.Map(location=[19, -12], zoom_start=2)   
    data = UserLocation.objects.all()

    for location_data in data:
        # Get the location and user from the UserLocation object
        location_name = location_data.Location
        user_name = location_data.User

        # Geocode the location to get latitude and longitude
        location = geocoder.osm(location_name)
        lat = location.lat
        lng = location.lng

        # Add marker to the map for each location
        folium.Marker([lat, lng], tooltip='Click for more', popup=f'{user_name} - {location_name}').add_to(m)

    # Convert the map to HTML representation
    m = m._repr_html_()

    return render(request, 'map.html', {'m' : m, 'loc': data})
