import geocode_api
import requests
import json 
import urllib.parse

api_key = "5b3ce3597851110001cf624892aea1aa581d4df29b49e12c43960ef9"
def distance(start_lon, start_lat, end_lon, end_lat):
    url_geocode_end = f"https://api.openrouteservice.org/geocode/search?api_key={api_key}"
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


    headers = {
        'Content-Type': 'application/json',
    }

    response_directions = requests.get(url_directions, headers=headers)

    
    if not (200 <= response_directions.status_code < 300):
        print("Error in Directions API:", response_directions.status_code)
        print("Response content:", response_directions.text)  
    else:
        directions_data = response_directions.json()
        distance = directions_data['routes'][0]['segments'][0]['distance']
        distance_km = distance / 1000
        