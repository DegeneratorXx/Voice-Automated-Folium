import folium

def create_map(coordinates, location_name):
    """Creates and saves a folium map centered on the given coordinates with a marker."""
    location_map = folium.Map(location=coordinates, zoom_start=13)
    folium.Marker(coordinates, popup=location_name).add_to(location_map)
    location_map.save('location_map.html')

def open_map():
    """Opens the generated map in the default web browser."""
    import webbrowser
    import os

    if os.path.isfile('location_map.html'):
        webbrowser.open('location_map.html')
    else:
        print("Map file not found.")
