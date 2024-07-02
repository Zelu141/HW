import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


# Параметризация для тестирования функции filter_by_currency
@pytest.mark.parametrize(
    "currency_code, expected_count", [("USD", 1), ("EUR", 1), ("JPY", 0)]  # предполагаем, что нет транзакций в JPY
)
def test_filter_by_currency(currency_code, expected_count):
    transactions = [
        {"operationAmount": {"amount": "1000", "currency": {"code": "USD"}}},
        {"operationAmount": {"amount": "2000", "currency": {"code": "EUR"}}},
        {"operationAmount": {"amount": "3000", "currency": {"code": "GBP"}}},
    ]
    filtered_transactions = list(filter_by_currency(transactions, currency_code))
    assert len(filtered_transactions) == expected_count


# Параметризация для тестирования функции transaction_descriptions
@pytest.mark.parametrize(
    "descriptions, expected",
    [
        ([{"description": "Перевод организации"}], ["Перевод организации"]),
        ([{"description": "Перевод со счета на счет"}], ["Перевод со счета на счет"]),
        ([], []),  # пустой список транзакций
    ],
)
def test_transaction_descriptions(descriptions, expected):
    descriptions_gen = transaction_descriptions(descriptions)
    assert list(descriptions_gen) == expected


# Параметризация для тестирования генератора card_number_generator
@pytest.mark.parametrize(
    "start, end, expected",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (
            9999,
            10001,
            ["0000 0000 0000 9999", "0000 0000 0001 0000", "0000 0000 0001 0001"],
        ),  # проверка на переход через границу
    ],
)
def test_card_number_generator(start, end, expected):
    card_numbers = list(card_number_generator(start, end))
    assert card_numbers == expected
