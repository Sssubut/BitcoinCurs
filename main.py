import requests

query = input('(usd - 1 | gbp - 2 | eur - 3) > ').upper()

if query == '1':
    query = 'usd'.upper()
elif query == '2':
    query = 'gbp'.upper()
elif query == '3':
    query = 'eur'.upper()

api_url = f'https://api.coindesk.com/v1/bpi/currentprice/{query}.json'
response = requests.get(api_url)

#Проверка запроса
if response.status_code == 200:

    print(f"BTC to {response.json()['bpi'][f'{query}']['code']}")
    print(f"Курс: {response.json()['bpi'][f'{query}']['rate']}")
