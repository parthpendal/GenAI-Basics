from mcp.server.fastmcp import FastMCP
from geopy.geocoders import Nominatim
import requests
import json

def get_lat_long_from_address(address_string)->tuple[float, float]:
    """
    Converts an address string into latitude and longitude coordinates.
    """
    # Initialize the Nominatim API geocoder, specifying a custom user_agent
    geolocator = Nominatim(user_agent="get_long_lat") # Replace with your app's name

    # Use the geocode method to get the location data for the address
    location = geolocator.geocode(address_string)

    if location:
        latitude = location.latitude
        longitude = location.longitude
        return latitude, longitude
    else:
        return None, None



def get_weather_from_longitude_lattitude(lat, lon)->str:
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
    return str(data["current"]["temperature_2m"])

mcp=FastMCP(name="Weather")

@mcp.tool()
def get_weather(city:str)->str:
    "This function will return the termperature for a given location"
    latitude, longitude = get_lat_long_from_address(city)
    return get_weather_from_longitude_lattitude(latitude, longitude)

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
#Streamable HTTP is a transport that allows you to stream the response from the server to the client.