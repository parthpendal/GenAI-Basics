from geopy.geocoders import Nominatim

def get_lat_long_from_address(address_string):
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

# Example usage:
address = "5 Lathrop Ln, Rocky Hill, CT 06067"
latitude, longitude = get_lat_long_from_address(address)

if latitude is not None and longitude is not None:
    print(f"Address: {address}")
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")
else:
    print(f"Could not find coordinates for the address: {address}")
