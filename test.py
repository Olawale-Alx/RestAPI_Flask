import requests


BASE: str = 'http://127.0.0.1:5000/'

response = requests.get(BASE + 'hello/kalipha')
print(response.json())
