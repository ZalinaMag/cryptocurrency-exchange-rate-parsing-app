import requests
import time

def fetch_price(pair_symbol):
    if pair_symbol == 'BTCUSDT':
        formatted_pair = 'BTC-USDT'
    else:
        formatted_pair = f'{pair_symbol[3:]}-BTC'

    url = f'https://api.kucoin.com/api/v1/market/orderbook/level1?symbol={formatted_pair}'
    
    for attempt in range(5):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()

                if data and 'data' in data and data['data'] is not None:
                    if 'price' in data['data']:
                        price = float(data['data']['price'])
                        
                        if pair_symbol != 'BTCUSDT':
                            return 1 / price
                        return price
                    else:
                        raise Exception(f"Отсутствует информация о цене для {pair_symbol}")
                else:
                    print(f"Данных нет для пары {pair_symbol} на KuCoin. Ответ: {data}")
                    return None
            else:
                print(f"Не удалось получить ответ для {pair_symbol}. Код состояния: {response.status_code}")
        except requests.Timeout:
            print(f"Таймаут запроса для {pair_symbol}. Повтор через 5 секунд.")
            time.sleep(5)
        except Exception as e:
            print(f"Произошла ошибка: {e}. Повтор через 5 секунд.")
            time.sleep(5)

    raise Exception(f"Не удалось получить данные для {pair_symbol} после нескольких попыток.")

def fetch_all_prices():
    pairs = ['BTCUSDT', 'BTCETH', 'BTCXMR', 'BTCSOL', 'BTCRUB', 'BTCDOGE']
    prices = {}

    for pair in pairs:
        try:
            price = fetch_price(pair)
            if price is not None:
                prices[pair] = price
                print(f"Текущий курс {pair} на KuCoin: {price}")
            else:
                print(f"Нет данных для {pair} на KuCoin.")
        except Exception as e:
            print(f"Ошибка при получении данных для {pair}: {e}")
    
    return prices

