import requests

def fetch_price(pair_symbol):
    url = f'https://api.binance.com/api/v3/ticker/price?symbol={pair_symbol}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        price = float(data['price'])

        if pair_symbol not in ['BTCUSDT', 'BTCRUB']:
            price = 1 / price

        return price
    else:
        raise Exception(f"Не удалось получить ответ для {pair_symbol}. Код состояния: {response.status_code}")

def fetch_all_prices():
    pairs = ['BTCUSDT', 'ETHBTC', 'XMRBTC', 'SOLBTC', 'BTCRUB', 'DOGEBTC']
    prices = {}

    for pair in pairs:
        try:
            price = fetch_price(pair)
            prices[pair] = price
            print(f"Текущий курс {pair} на Binance: {price}")
        except Exception as e:
            print(e)
    
    return prices

all_prices = fetch_all_prices()
