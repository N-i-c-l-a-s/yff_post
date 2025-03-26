import json
import requests
import urllib.parse

start = input("Enter the place name (start): ")
end = input("Enter the destination name (end): ")

encoded_place_name = urllib.parse.quote(start)
encoded_destination_name = urllib.parse.quote(end)

api_key = "5b3ce3597851110001cf624892aea1aa581d4df29b49e12c43960ef9"

# Get coordinates for the start location
url_geocode_start = f"https://api.openrouteservice.org/geocode/search?api_key={api_key}&text={encoded_place_name}"
response_start = requests.get(url_geocode_start)

if response_start.status_code == 200:
    data_start = response_start.json()
    start_coordinates = data_start['features'][0]['geometry']['coordinates']
    start_lon, start_lat = start_coordinates
    print(f"Start coordinates (longitude, latitude): Longitude = {start_lon}, Latitude = {start_lat}")
else:
    print("Error in geocoding start location: ", response_start.status_code)

# Get coordinates for the destination location
url_geocode_end = f"https://api.openrouteservice.org/geocode/search?api_key={api_key}&text={encoded_destination_name}"
response_end = requests.get(url_geocode_end)

if response_end.status_code == 200:
    data_end = response_end.json()
    end_coordinates = data_end['features'][0]['geometry']['coordinates']
    end_lon, end_lat = end_coordinates
    print(f"End coordinates (longitude, latitude): Longitude = {end_lon}, Latitude = {end_lat}")
else:
    print("Error in geocoding destination location: ", response_end.status_code)

# Prepare the directions URL (correct longitude, latitude format)
url_directions = f"https://api.openrouteservice.org/v2/directions/driving-car?api_key={api_key}&start={start_lat},{start_lon}&end={end_lat},{end_lon}"

# Debug: Print the constructed URL
print(f"Requesting directions with URL: {url_directions}")


headers = {
    'Content-Type': 'application/json',
}

response_directions = requests.get(url_directions, headers=headers)

# Check for a successful response
if not (200 <= response_directions.status_code < 300):
    print("Error in Directions API:", response_directions.status_code)
    print("Response content:", response_directions.text)  
else:
    directions_data = response_directions.json()
    distance = directions_data['routes'][0]['segments'][0]['distance']
    distance_km = distance / 1000
    print(f"Distance between {start} and {end}: {distance_km:.2f} km")
