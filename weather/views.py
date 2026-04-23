from django.shortcuts import render
from django.http import JsonResponse
import requests

API_KEY = "482ba1bc49552d5b6f6864d931626ff0"

def home(request):
    return render(request, "index.html")

def get_weather(request):
    city = request.GET.get('city')

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    print(data)

    if data.get("cod") != 200:
        return JsonResponse({"error": "City not found"})

    weather_data = {
        "city": city,
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "icon": data["weather"][0]["icon"]
    }

    return JsonResponse(weather_data)