import folium
from geopy.geocoders import Nominatim
from streamlit_folium import st_folium


def show_map(destination):  # noqa: Vulture
    """
    Display destination on an interactive map.
    """

    try:
        geolocator = Nominatim(user_agent="ai_travel_planner")

        location = geolocator.geocode(destination)

        if not location:
            return False

        latitude = location.latitude
        longitude = location.longitude

        travel_map = folium.Map(location=[latitude, longitude], zoom_start=12)

        folium.Marker(
            [latitude, longitude], popup=destination, tooltip=destination
        ).add_to(travel_map)

        st_folium(travel_map, width=700, height=450)

        return True

    except Exception:
        return False
