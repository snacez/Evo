import requests

url = 'https://wttr.in'

weather_parameters = {
    '0': '',
    'T': '',
    'M': '',
}

request_headers = {
    'Accept-Language': 'ru'  # задайте русский язык через заголовок
}

response = requests.get(url, params=weather_parameters, headers=request_headers)  # передайте параметры и заголовки в http-запрос

print(response.text)