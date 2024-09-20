import requests

def fetch_price(pair_symbol):
    url = f'https://api.bybit.com/v2/public/tickers?symbol={pair_symbol}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        price = float(data['result'][0]['last_price'])
        return price
    else:
        raise Exception(f"Не удалось получить ответ для {pair_symbol} на Bybit. Превышен лимит запросов. Код состояния: {response.status_code}")

def fetch_all_prices():
    pairs = ['BTCUSDT', 'BTCETH', 'BTCXMR', 'BTCSOL', 'BTCRUB', 'BTCDOGE']
    prices = {}

    for pair in pairs:
        try:
            price = fetch_price(pair)
            prices[pair] = price
            print(f"Текущий курс {pair} на Bybit: {price}")
        except Exception as e:
            print(e)
    
    return prices
