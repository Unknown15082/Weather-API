import requests
from dotenv import load_dotenv
import os

def forecast(location, lang = "en"):
    """
    Syntax: forecast((<latitude>, <longitude>), <language = "en">)

    Get the weather forecast of the specified location.
    """

    load_dotenv()
    KEY = os.environ["APIKEY"]
    
    parameters = dict()

    lat, lon = location
    parameters["lat"] = str(lat)
    parameters["lon"] = str(lon)
    parameters["units"] = "metric"
    parameters["exclude"] = "minutely,alerts"
    parameters["appid"] = KEY

    url = f"https://api.openweathermap.org/data/2.5/onecall"

    data = requests.get(url, params = parameters)
    data = data.json()

    return data