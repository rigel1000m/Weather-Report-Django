from django.shortcuts import render, redirect
from .models import LastReport
from .templates import *
from .forms import LastReportForms
import requests
import json

# Create your views here.

def home(request):
    appID = 'fcc34f76391e1ada35572d79579405fe'
    city = ''

    if(request.method == 'POST'):
        form = LastReportForms(request.POST)
        if form.is_valid():
            form.save()
            city = request.POST.get('city', '')
#             return redirect('home')

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print('YOUR IP IS -------→ ' + ip)

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid={appID}"

    form = LastReportForms()

    response = requests.get(url)
    print(response.status_code)
    if response.status_code == 404 or response.status_code == 400:
        context = {
            'form': form,
            'error': 'Проверьте правильность указания города'
        }
        return render(request, 'home.html', context=context)
    else:
        response = response.json()
        context = {
            'city_name': response['name'],
            'description': response['weather'][0]['description'],
            'temperature': response['main']['temp'],
            'feels_like': int(response['main']['feels_like']),
            'wind_speed': int(response['wind']['speed']),
            'icon': response['weather'][0]['icon'],
            'form': form,
            'ip': ip,
            'error': ''
        }
        return render(request, 'home.html', context=context)
