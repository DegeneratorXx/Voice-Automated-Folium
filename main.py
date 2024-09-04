import time
from speech_utils import recognize_speech
from geo_utils import get_coordinates
from map_utils import create_map, open_map

def main():
    while True:
        location_name = recognize_speech()
        if location_name=="stop":
            break
        if location_name:
            coordinates = get_coordinates(location_name)
            if coordinates:
                create_map(coordinates, location_name)
                open_map()
                
        time.sleep(10) 

if __name__ == "__main__":
    main()
