import requests
import json
api_key = "5b3ce3597851110001cf624892aea1aa581d4df29b49e12c43960ef9"
def snap_api(start_lon, start_lat, end_lon, end_lat):
    SNAP_URL = "https://api.openrouteservice.org/v2/snap/driving-car"
    body = {"locations": [[start_lon, start_lat], [end_lon, end_lat]]}
    headers = {'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'}
    
    response = requests.post(SNAP_URL, json=body, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        print("API Response:", json.dumps(data, indent=4))  

        
        snapped_start = data["locations"][0]
        snapped_end = data["locations"][1]

        if snapped_start is None:
            print("Warning: Start location could not be snapped!")
        else:
            snapped_start_lon, snapped_start_lat = snapped_start["location"]
            print(f"Snapped Start Coordinates: {snapped_start_lon}, {snapped_start_lat}")

        if snapped_end is None:
            print("Warning: End location could not be snapped!")
        else:
            snapped_end_lon, snapped_end_lat = snapped_end["location"]
            print(f"Snapped End Coordinates: {snapped_end_lon}, {snapped_end_lat}")
    
    else:
        print(f"Error: {response.status_code}, {response.text}")
