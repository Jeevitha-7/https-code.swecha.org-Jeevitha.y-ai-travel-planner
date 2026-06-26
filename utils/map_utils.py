import folium
from geopy.geocoders import Nominatim

DEFAULT_LOCATION = [20.5937, 78.9629]


def get_map(location: str = "India"):
    # FIX: handle empty input safely
    if not location:
        location = "India"

    geolocator = Nominatim(user_agent="travel_app")
    try:
        loc = geolocator.geocode(location)

        # fallback if geocoding fails
        if not loc:
            loc = geolocator.geocode("India")
    except Exception:
        loc = None

    if not loc:
        return folium.Map(location=DEFAULT_LOCATION, zoom_start=5)

    m = folium.Map(location=[loc.latitude, loc.longitude], zoom_start=5)
    return m
