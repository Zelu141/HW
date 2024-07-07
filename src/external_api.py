import requests
import os


def convert_currency(amount, currency):
    if currency not in ['USD', 'EUR']:
        return amount

    api_key = os.getenv('fcjtF6N2gmxUZM5i3pxv8wtR6XL3uDaX')
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
    headers = {
        "apikey": api_key
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()['result']
    else:
        raise Exception("API request failed")


if __name__ == '__main__':
    print(convert_currency(6, 5))