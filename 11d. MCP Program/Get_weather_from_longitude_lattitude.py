import requests
import json

# Coordinates for Rocky Hill, CT
lat = 41.66
lon = -72.63

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": lat,
    "longitude": lon,
    "current": "temperature_2m,wind_speed_10m",
    "temperature_unit": "fahrenheit",
    "timezone": "America/New_York"
}

response = requests.get(url, params=params)
data = response.json()
# ... after getting your 'data' variable ...
print(json.dumps(data, indent=4))

print(data["current"]["temperature_2m"])
