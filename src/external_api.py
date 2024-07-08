import requests
import os
from dotenv import load_dotenv

load_dotenv('.env')


def convert_currency(operation):
    # Проверка на RUB и возврат суммы, если валюта - RUB
    if operation["operationAmount"]["currency"]["code"] == "RUB":
        return float(operation["operationAmount"]["amount"])

    # Получение суммы и кода валюты из словаря
    amount = operation["operationAmount"]["amount"]
    currency_code = operation["operationAmount"]["currency"]["code"]

    # Конвертация валюты (здесь должна быть логика конвертации)
    # Например, использование внешнего API для получения курса валюты
    # converted_amount = amount * get_exchange_rate(currency_code)

    # Возвращаем сконвертированную сумму как float
    # return float(converted_amount)
    # Заглушка для примера, замените на реальную логику конвертации
    return float(amount) * 1.1  # Пример умножения на курс
    api_key = os.getenv("API_KEY")
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
    headers = {"apikey": api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()["result"]
    else:
        raise Exception("API request failed")
