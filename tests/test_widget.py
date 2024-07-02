import pytest
from datetime import datetime
from src.widget import mask_account_card, get_data


def test_mask_account_card_valid_account():
    # Тест для проверки маскировки номера счета
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"


def test_mask_account_card_valid_card():
    # Тест для проверки маскировки номера карты
    assert mask_account_card("7365410843013587") == "7365 79** **** 3587"


@pytest.mark.parametrize(
    "invalid_input",
    [
        "Неверный формат 123",
        "12345",  # Слишком короткий
        "abcdefg123456789",  # Содержит буквы
        # Добавьте другие неверные форматы по вашему выбору
    ],
)
def test_mask_account_card_invalid_format(invalid_input):
    with pytest.raises(ValueError):
        mask_account_card(invalid_input)


def test_get_data():
    # Предполагаемая дата в формате ISO 8601
    input_date = "2024-07-01T11:59:35.123456"
    # Ожидаемый результат после преобразования
    expected_date = "01.07.2024"
    # Вызов функции get_data
    result = get_data(input_date)
    # Проверка результата
    assert result == expected_date, f"Ожидаемая дата {expected_date}, получена дата {result}"
