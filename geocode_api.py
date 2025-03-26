import requests
import urllib.parse

api_key = "5b3ce3597851110001cf624892aea1aa581d4df29b49e12c43960ef9"

def geocode(start, end):
    # Ensure inputs are not empty
    if not start or not end:
        print("Error: Start or End location is empty.")
        return None

    # Encode place names for safe URL usage
    encoded_start = urllib.parse.quote(start)
    encoded_end = urllib.parse.quote(end)

    # Build API request URLs
    url_geocode_start = f"https://api.openrouteservice.org/geocode/search?api_key={api_key}&text={encoded_start}"
    url_geocode_end = f"https://api.openrouteservice.org/geocode/search?api_key={api_key}&text={encoded_end}"

    # Send requests
    response_start = requests.get(url_geocode_start)
    response_end = requests.get(url_geocode_end)

    # Debugging: Print full API responses
    print("Start Location API Response:", response_start.text)
    print("End Location API Response:", response_end.text)

    # Handle responses
    if response_start.status_code == 200 and response_end.status_code == 200:
        data_start = response_start.json()
        data_end = response_end.json()

        
        if "features" not in data_start or len(data_start["features"]) == 0:
            print("Error: No results found for start location.")
            return None
        if "features" not in data_end or len(data_end["features"]) == 0:
            print("Error: No results found for end location.")
            return None

        
        start_coordinates = data_start["features"][0]["geometry"]["coordinates"]
        end_coordinates = data_end["features"][0]["geometry"]["coordinates"]

        return start_coordinates[1], start_coordinates[0], end_coordinates[1], end_coordinates[0]

    else:
        print(f"Geocoding Error: {response_start.status_code} (Start), {response_end.status_code} (End)")
        return None
