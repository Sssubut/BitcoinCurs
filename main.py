import requests

api_url = 'https://660a65c90f324a9a2884e818.mockapi.io/users'

response = requests.get(api_url)
#Проверка запроса.
if response.status_code == 200:
    print(print(response.json()))
else:
    print(response.status_code)
