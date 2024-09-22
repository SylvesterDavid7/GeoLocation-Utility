import requests
import argparse
import sys

API_KEY = 'f897a99d971b5eef57be6fafa0d83239'
BASE_URL = 'http://api.openweathermap.org/geo/1.0/'

def get_geolocation(query):
    if query.isdigit():
        # Query by Zip Code
        url = f'{BASE_URL}zip?zip={query},US&appid={API_KEY}'
    else:
        # Query by City/State
        city, state = query.split(',')
        url = f'{BASE_URL}direct?q={city.strip()},{state.strip()},US&limit=1&appid={API_KEY}'

    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data for {query}: {response.status_code}")
        return None

def parse_geolocation(data, query):
    if isinstance(data, list) and len(data) > 0:
        place = data[0]
        return {
            'query': query,
            'latitude': place['lat'],
            'longitude': place['lon'],
            'place_name': place.get('name', 'Unknown')
        }
    elif isinstance(data, dict):
        return {
            'query': query,
            'latitude': data['lat'],
            'longitude': data['lon'],
            'place_name': data.get('name', 'Unknown')
        }
    return None

def main():
    parser = argparse.ArgumentParser(description="Get geolocation data for city/state or zip code")
    parser.add_argument('--locations', nargs='+', required=True, help="List of locations (e.g., 'Madison, WI', '12345')")

    args = parser.parse_args()

    for query in args.locations:
        data = get_geolocation(query)
        if data:
            result = parse_geolocation(data, query)
            if result:
                print(f"{result['query']}: {result['place_name']}, Lat: {result['latitude']}, Lon: {result['longitude']}")
            else:
                print(f"No results found for {query}")

if __name__ == '__main__':
    main()
