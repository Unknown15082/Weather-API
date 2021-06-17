import requests
from dotenv import load_dotenv
import os

def getcurrent(location, lang = "en"):
    """
    Syntax: getcurrent((<latitude>, <longitude>), <language = "en">)

    Get the data of the current weather at the specified location.
    """

    load_dotenv()
    KEY = os.environ["APIKEY"]
    
    parameters = dict()

    lat, lon = location
    parameters["lat"] = str(lat)
    parameters["lon"] = str(lon)
    parameters["units"] = "metric"
    parameters["appid"] = KEY

    url = f"https://api.openweathermap.org/data/2.5/weather"

    data = requests.get(url, params = parameters)
    data = data.json()

    return data

