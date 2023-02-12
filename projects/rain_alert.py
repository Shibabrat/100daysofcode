import requests
import os

# check open weather map for API, then export to the python environment variable
API_KEY = os.environ.get("OWM_API_KEY")

# Zeeman building, Warwick campus
LATITUDE = 52.383981
LONGITUDE = -1.559391

# https://openweathermap.org/forecast5: 5 day forecast with 3 hour step
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": API_KEY,
}

will_rain = False

if API_KEY is not None:
    response = requests.get(OWM_ENDPOINT, params=weather_params)
    weather_data = response.json()
    # print(weather_data)
    # print(weather_data["list"][0]["weather"][0]["id"])
    weather_slice = weather_data["list"][:5]
    for hour_data in weather_slice:
        condition_code = hour_data["weather"][0]["id"]
        if int(condition_code) < 700:
            will_rain = True


    if will_rain:
        print("Bring an umbrella")
    else:
        print("No need for an umbrella!")


# Email or text the notification.


