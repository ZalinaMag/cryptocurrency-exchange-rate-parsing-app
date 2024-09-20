import requests

API_KEY = 'your_coinmarketcap_api_key'

def fetch_price(pair_symbol):
    url = f'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol={pair_symbol[:3]}&convert={pair_symbol[3:]}'
    headers = {
        'X-CMC_PRO_API_KEY': API_KEY,
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        price = float(data['data'][pair_symbol[:3]]['quote'][pair_symbol[3:]]['price'])
        return price
    else:
        raise Exception(f"Не удалось получить ответ для {pair_symbol}. Код состояния: {response.status_code}")

def fetch_all_prices():
    pairs = ['BTCUSDT', 'BTCETH', 'BTCXMR', 'BTCSOL', 'BTCRUB', 'BTCDOGE']
    prices = {}

    for pair in pairs:
        try:
            price = fetch_price(pair)
            prices[pair] = price
            print(f"Текущий курс {pair} на CoinMarketCap: {price}")
        except Exception as e:
            print(e)
    
    return prices
