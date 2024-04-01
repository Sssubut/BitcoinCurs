import requests

api_url = 'https://660a65c90f324a9a2884e818.mockapi.io/users'

response = requests.get(api_url)

if response.status_code == 200:
    # Если код ответа на запрос - 200, то смотрим, что пришло в ответе
    print(print(response.json()))
else:
    print(response.status_code)    # При другом коде ответа выводим этот код
