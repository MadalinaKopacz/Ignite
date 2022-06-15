from django.shortcuts import render
from datetime import datetime
import requests
from accounts.views import get_streaks
from django.contrib.gis.geoip2 import GeoIP2


def get_time(request):
    """
    method that gets the server time at request
    """
    current_datetime = datetime.now()  
    time = current_datetime.strftime("%I:%M %p")
    return time


def get_temperature(request):
    """
    method that gets weather details from the ip using an API
    """
    key = "9fa76c16db4ea6572cdc950e6ec3ed42"
    city = ""

    g = GeoIP2() # to compute location from ip/city

    # ip = request.META.get('REMOTE_ADDR', None)
    ip = '86.121.188.6' # because server runs on local host
    if ip:
        city = g.city(ip)['city']
    else:
        city = 'Bucharest' 

    url1 = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={key}"

    r1 = requests.get(url1).json() # get data from api
    lon = r1[0]["lon"]
    lat = r1[0]["lat"]

    url2 = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}"
    r2 = requests.get(url2).json()
    city_weather = {
        'city': city,
        'temperature': [r2['main']['temp'], int(r2['main']['temp'] - 273.15), int(1.8 * (r2['main']['temp'] - 273) + 32)],
        'description': r2['weather'][0]['description'],
        'icon': f"https://openweathermap.org/img/wn/{r2['weather'][0]['icon']}@2x.png"
    }

    return city_weather


def get_data(request):
    """
    method that computes the data needed to render start page
    """
    if request.user.is_anonymous: # User isn't logged in
        return render(request, "global/index.html")

    time = get_time(request)
    city_weather = get_temperature(request)
    streaks = get_streaks(request)
    return render(request, "global/start_page.html", {"time" : time, "weather" : city_weather, "streaks": streaks})
