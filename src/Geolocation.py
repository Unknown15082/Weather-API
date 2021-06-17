from geopy.geocoders import Nominatim

def geo(name):

    """
    Syntax: geo(<name of location>)

    Return the latitude and longitude of the specified location.
    """

    client = Nominatim(user_agent = "geolocation")
    location = client.geocode(name).raw

    return int(location["lat"]), int(location["lon"])

def revgeo(lat, lon, lang = "en"):

    """
    Syntax: revgeo(<latitude>, <longitude>, language = "en")

    Return the name of location specified by latitude & longitude
    """

    client = Nominatim(user_agent = "reverse geolocation")
    location = client.reverse(f"{lat}, {lon}", language = lang).raw

    return location["display_name"]