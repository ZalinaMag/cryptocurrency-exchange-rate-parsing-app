from exchange.binance import fetch_all_prices as fetch_binance_prices
# from exchange.coinmarketcap import fetch_all_prices as fetch_coinmarketcap_prices
from exchange.bybit import fetch_all_prices as fetch_bybit_prices
from exchange.gateio import fetch_all_prices as fetch_gateio_prices
from exchange.kucoin import fetch_all_prices as fetch_kucoin_prices
from services.email_sender import send_email
from database.crud import create_key_json
from datetime import datetime
import logging

async def process_prices(previous_totals):
    try:
        all_prices = {}

        try:
            all_prices['Binance'] = fetch_binance_prices()
        except Exception as e:
            print(f"Ошибка при получении данных с Binance: {e}", flush=True)

        # try:
        #     all_prices['CoinMarketCap'] = fetch_coinmarketcap_prices()
        # except Exception as e:
        #     print(f"Ошибка при получении данных с CoinMarketCap: {e}", flush=True)

        try:
            all_prices['Gate.io'] = fetch_gateio_prices()
        except Exception as e:
            print(f"Ошибка при получении данных с Gate.io: {e}", flush=True)

        try:
            all_prices['KuCoin'] = fetch_kucoin_prices()
        except Exception as e:
            print(f"Ошибка при получении данных с KuCoin: {e}", flush=True)

        try:
            all_prices['Bybit'] = fetch_bybit_prices()
        except Exception as e:
            print(f"Ошибка при получении данных с Bybit: {e}", flush=True)

        if not all_prices:
            print("Нет успешных данных с бирж, пропускаем итерацию.", flush=True)
            return previous_totals

        results = {}
        for pair in all_prices.get('Binance', {}).keys():
            valid_prices = [all_prices[exchange][pair] for exchange in all_prices if pair in all_prices[exchange]]

            if not valid_prices:
                print(f"Не удалось получить данные для {pair} на всех биржах.", flush=True)
                continue

            best_price = max(valid_prices)
            best_exchange = max(all_prices, key=lambda e: all_prices[e].get(pair, 0))

            total = best_price * 3
            previous_total = previous_totals.get(pair)

            if previous_total is None:
                difference = 0
                percent_change = 0
            else:
                difference = total - previous_total
                percent_change = (difference / previous_total) * 100

            second_currency = pair.replace('BTC', '')

            if percent_change >= 0.03 or previous_total is None:
                print(f"Текущий курс {pair} на {best_exchange} для 3 BTC: {total:.2f} {second_currency}", flush=True)
                print(f"Разница с предыдущей суммой: {difference:.2f} {second_currency}", flush=True)
                print(f"Процент изменения: {percent_change:.5f}%", flush=True)

                subject = f"Изменение курса {pair} на {best_exchange}"
                body = (
                    f"Текущий курс {pair} на {best_exchange} для 3 BTC: {total:.2f} {second_currency}\n"
                    f"Разница с предыдущей суммой: {difference:.2f} {second_currency}\n"
                    f"Процент изменения: {percent_change:.5f}%"
                )
                send_email(subject, body)

                data = {
                    "title": f"{pair} Update",
                    "kash": [{"price": str(best_price), "minmax": [{"max price": str(total), "min price": str(previous_total if previous_total else 0)}]}],
                    "difference": str(difference),
                    "total amount": str(total),
                    "coins": [{"BTC": second_currency}],
                    "date": datetime.now().isoformat()
                }

                try:
                    await create_key_json(data)
                    print(f"Данные для {pair} успешно сохранены в БД.", flush=True)

                except Exception as e:
                    error_message = f"Ошибка при сохранении данных для {pair}: {e}"
                    logging.error(error_message)
                    print(error_message, flush=True)

            results[pair] = total

        return results
    except Exception as e:
        print(f"Произошла ошибка: {e}", flush=True)
        return previous_totals

