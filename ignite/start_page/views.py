from django.shortcuts import render
from datetime import datetime

from django.contrib.gis.utils import GeoIP2



def get_time(request):
    current_datetime = datetime.now()  
    time = current_datetime.strftime("%I:%M %p")
    return time

def get_temperature(request):
    key = "9fa76c16db4ea6572cdc950e6ec3ed42"
    city = ""

    g = GeoIP2()

    ip = request.META.get('REMOTE_ADDR', None)
    if ip:
        city = g.city(ip)['city']
    else:
        city = 'Bucharest' 

    url1 = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={key}"


    r1 = request.get(url1).json()
    lon = r1["lon"]
    lat = r1["lat"]

    url2 = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}"
    r2 = request.get(url2).json()
    city_weather = {
        'city': city,
        'temperature': r2['main']['temp'],
        'description': r2['weather'][0]['description'],
        'icon': r2['weather'][0]['icon']
    }

    return city_weather

def get_data(request):
    time = get_time(request)
    city_weather = get_temperature(request)

    return render(request, "", {"time" : time, "weather" : city_weather})
