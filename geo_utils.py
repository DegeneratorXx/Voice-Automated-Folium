from geopy.geocoders import Nominatim

# Initialize the geolocator
geolocator = Nominatim(user_agent="geoapiExercises")

def get_coordinates(location_name):
    """Converts a location name into geographic coordinates using Nominatim."""
    try:
        location = geolocator.geocode(location_name)
        if location:
            return [location.latitude, location.longitude]
        else:
            print("Location not found.")
            return None
    except Exception as e:
        print(f"Error occurred: {e}")
        return None
