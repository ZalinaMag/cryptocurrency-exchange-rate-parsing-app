import requests

def fetch_price(pair_symbol):
    if pair_symbol == 'BTCUSDT':
        formatted_pair = 'btc_usdt'
    else:
        formatted_pair = pair_symbol[3:].lower() + '_btc'

    url = f'https://api.gateio.ws/api/v4/spot/tickers?currency_pair={formatted_pair}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        price = float(data[0]['last'])

        if pair_symbol != 'BTCUSDT':
            price = 1 / price
        
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
            print(f"Текущий курс {pair} на Gate.io: {price}")
        except Exception as e:
            print(f"Ошибка при запросе {pair}: {e}")
    
    return prices

all_prices = fetch_all_prices()
