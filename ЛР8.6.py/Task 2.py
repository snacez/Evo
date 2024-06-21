import requests

url = 'https://wttr.in'  # не изменяйте значение URL

weather_parameters = {
    '0': '',
    'T': '',  # параметр запроса `T`, чтобы вернулся чёрно-белый текст
    'M': '',  # параметр запроса `M`, чтобы скорость ветра была в м/с
    'lang': 'ru'  # параметр запроса `lang` со значением `ru` для получения прогноза на русском языке
}

response = requests.get(url, params=weather_parameters)  # передайте параметры в http-запрос

print(response.text)