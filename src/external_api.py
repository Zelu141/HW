import os

import requests


def convert_to_rub(amount: float, currency: str) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    :param amount: Сумма транзакции.
    :param currency: Валюта транзакции ('USD', 'EUR', 'RUB').
    :return: Сумма транзакции в рублях.
    :raises Exception: Если запрос к API не удался.
    """
    if currency == 'RUB':
        return amount

    access_key = os.getenv('API_KEY')
    url = f'https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}'
    headers = {'apikey': access_key}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('result', 0.0)
    else:
        raise Exception('API request failed with status code: ' + str(response.status_code))
