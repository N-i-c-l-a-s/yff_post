import geocode_api
import requests
import json 
import urllib.parse
import geocode_api
import distance_api
import snap_api

api_key = "5b3ce3597851110001cf624892aea1aa581d4df29b49e12c43960ef9"


start = input("Enter the place name (start): ")
end = input("Enter the destination name (end): ")


def main():
    
    start_lon, start_lat, end_lon, end_lat = geocode_api.geocode(start, end)
    
    if start_lon is not None and end_lon is not None:
        
        distance_api.distance(start_lon, start_lat, end_lon, end_lat)
        
        
        snap_api.snap_api(start_lon, start_lat, end_lon, end_lat)


if __name__ == "__main__":
    main()
