from django.shortcuts import render
from datetime import datetime
import requests

from django.contrib.gis.geoip2 import GeoIP2


def get_time(request):
    current_datetime = datetime.now()  
    time = current_datetime.strftime("%I:%M %p")
    return time

def get_temperature(request):
    key = "9fa76c16db4ea6572cdc950e6ec3ed42"
    city = ""

    g = GeoIP2()

    # ip = request.META.get('REMOTE_ADDR', None)
    ip = '86.121.188.6'
    if ip:
        city = g.city(ip)['city']
    else:
        city = 'Bucharest' 

    url1 = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={key}"


    r1 = requests.get(url1).json()
    print(r1)
    lon = r1[0]["lon"]
    lat = r1[0]["lat"]

    url2 = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}"
    r2 = requests.get(url2).json()
    city_weather = {
        'city': city,
        'temperature': r2['main']['temp'],
        'description': r2['weather'][0]['description'],
        'icon': f"https://openweathermap.org/img/wn/{r2['weather'][0]['icon']}@2x.png"
    }

    return city_weather

def get_data(request):
    time = get_time(request)
    city_weather = get_temperature(request)

    return render(request, "global/start_page.html", {"time" : time, "weather" : city_weather})
