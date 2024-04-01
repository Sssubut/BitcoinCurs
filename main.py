import requests

query = input('(usd/gbp/eur) > ').upper()

api_url = f'https://api.coindesk.com/v1/bpi/currentprice/{query}.json'
response = requests.get(api_url)

#Проверка запроса
if response.status_code == 200:
    # print(print(response.json()))

    print(f'BTC to {response.json()['bpi'][f'{query}']['code']}')
    print(f'Курс: {response.json()['bpi'][f'{query}']['rate']}')


