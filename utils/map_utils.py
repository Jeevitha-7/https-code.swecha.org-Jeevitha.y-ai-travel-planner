import folium
from geopy.geocoders import Nominatim


def get_map(location: str = "India"):
    # FIX: handle empty input safely
    if not location:
        location = "India"

    geolocator = Nominatim(user_agent="travel_app")
    loc = geolocator.geocode(location)

    # fallback if geocoding fails
    if not loc:
        loc = geolocator.geocode("India")

    if not loc:
        return None

    m = folium.Map(location=[loc.latitude, loc.longitude], zoom_start=5)
    return m
