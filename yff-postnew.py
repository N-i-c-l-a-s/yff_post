import json
import requests
import urllib.parse

start = input("Enter the place name (start): ")
end = input("Enter the destination name (end): ")

encoded_place_name = urllib.parse.quote(start)
encoded_destination_name = urllib.parse.quote(end)

api_key = "5b3ce3597851110001cf624892aea1aa581d4df29b49e12c43960ef9"

headers = {
    "Authorization": api_key,
    "Content-Type": "application/json"
}


url_geocode_start = f"https://api.openrouteservice.org/geocode/search?api_key={api_key}&text={encoded_place_name}"
response_start = requests.get(url_geocode_start)

if response_start.status_code == 200:
    data_start = response_start.json()
    start_coordinates = data_start['features'][0]['geometry']['coordinates']
    start_lon, start_lat = start_coordinates
    print(f"Start coordinates (longitude, latitude): Longitude = {start_lon}, Latitude = {start_lat}")
else:
    print("Error in geocoding start location: ", response_start.status_code)


url_geocode_end = f"https://api.openrouteservice.org/geocode/search?api_key={api_key}&text={encoded_destination_name}"
response_end = requests.get(url_geocode_end)

if response_end.status_code == 200:
    data_end = response_end.json()
    end_coordinates = data_end['features'][0]['geometry']['coordinates']
    end_lon, end_lat = end_coordinates
    print(f"End coordinates (longitude, latitude): Longitude = {end_lon}, Latitude = {end_lat}")
else:
    print("Error in geocoding destination location: ", response_end.status_code)


SNAP_URL = "https://api.openrouteservice.org/v2/snap/driving-car"

body = {
    "locations": [
        [start_lon, start_lat],  
        [end_lon, end_lat]       
    ]
}

response = requests.post(SNAP_URL, json=body)


if response.status_code == 200:
    data = response.json()
    
    
    snapped_start_lon, snapped_start_lat = data["snapped_points"][0]["location"]
    snapped_end_lon, snapped_end_lat = data["snapped_points"][1]["location"]
    
    print(f"Snapped Start Coordinates: Longitude = {snapped_start_lon}, Latitude = {snapped_start_lat}")
    print(f"Snapped End Coordinates: Longitude = {snapped_end_lon}, Latitude = {snapped_end_lat}")
else:
    print(f"Error: {response.status_code}, {response.text}")
