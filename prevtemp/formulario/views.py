import requests 
import json
import csv
from django import forms
from django.shortcuts import render
from .models import Tempo
# Create your views here.
def formulario(request):
    
    print(request.GET.get('cidade'))
    cityname = request.GET.get('cidade')
    api_key = 'f4fd48a14fbc3515ce08b19319cb6a16'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={api_key}'

    response = requests.get(url)
    response = response.json()
    print(type(response))
    print(response['main'])
    list = ['temp', 'feels_like', 'temp_min', 'temp_max', 'pressure', 'humidity']
    tempo = Tempo()
    tempo.temp = response['main']['temp']
    tempo.feels_like = response['main']['feels_like']
    tempo.temp_min = response['main']['temp_min']
    tempo.temp_max = response['main']['temp_max']
    tempo.pressure = response['main']['pressure']
    tempo.humidity = response['main']['humidity']
    tempo.save()
    tempo = Tempo.objects.all()
    return render(request, 'index.html', {'dados': tempo})



def importardados(request):
    cityname = 'João Pessoa'
    api_key = 'f4fd48a14fbc3515ce08b19319cb6a16'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={api_key}'

    response = requests.get(url)
    response = response.json()
    print(type(response))
    print(response['main'])
    list = ['temp', 'feels_like', 'temp_min', 'temp_max', 'pressure', 'humidity']
    tempo = Tempo()
    tempo.temp = response['main']['temp']
    tempo.feels_like = response['main']['feels_like']
    tempo.temp_min = response['main']['temp_min']
    tempo.temp_max = response['main']['temp_max']
    tempo.pressure = response['main']['pressure']
    tempo.humidity = response['main']['humidity']
    tempo.save()
    return render(request, '')
    """ with open ('formulario/templates/dados.csv', 'w', newline='') as test:
        conteudo = csv.writer(test)
        conteudo.writerow(list)
        x = [str(response['main'][item]) for item in list]
        conteudo.writerow(x) """ 

    """ with open ('formulario/templates/dados.csv', 'r') as f:
        ler_csv = csv.DictReader(f)
        
        for linha in ler_csv:
            #pegando o valor de temperatura e convertendo em celisius
            temp = (linha['temp'])
            temp = float(temp)
            temp = int(temp)
            temp_celsius = temp - 273
            #pegando o valor de temperatura e convertendo em celisius
            feels_like = (linha['feels_like'])
            feels_like = float(feels_like)
            feels_like = int(feels_like)
            feels_like_celsius = feels_like - 273
        
            temp_min = (linha['temp_min'])
            temp_min = float(temp_min)
            temp_min = int(temp_min)
            temp_min_celsius = temp_min - 273
        
            temp_max = (linha['temp_max'])
            temp_max = float(temp_max)
            temp_max = int(temp_max)
            temp_max_celsius = temp_max - 273
        
            pressure = (linha['pressure'])
            pressure = float(pressure)

            humidity = (linha['humidity'])
            humidity = int(humidity)
            
            
            dict_dados = {
            "temp" : temp_celsius,
            "feels_like" : feels_like_celsius,
            "temp_min": temp_min_celsius,
            "temp_max": temp_max_celsius,
            "pressure" : pressure,
            "humidity" : humidity
            }
            print(dict_dados)
            with open('formulario/templates/dadoscelisius.csv', 'w', newline='') as test:
                conteudo = csv.writer(test)
                conteudo.writerow(list)
                x= [str(dict_dados[f'{i}']) for i in list]
                conteudo.writerow(x) 






 """