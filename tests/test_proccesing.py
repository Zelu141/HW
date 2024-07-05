
import pytest

from src.processing import filter_by_state, sort_by_date

# Тестовые данные
test_data = [
    {"id": 1, "state": "EXECUTED"},
    {"id": 2, "state": "PENDING"},
    {"id": 3, "state": "CANCELED"},
    {"id": 4, "state": "EXECUTED"},
]


# Фикстура для тестовых данных
@pytest.fixture
def input_data():
    return test_data.copy()


# Тесты для функции filter_by_state
def test_filter_by_state_default(input_data):
    """
    Тест проверяет работу функции с параметром state по умолчанию.
    """
    result = filter_by_state(input_data)
    assert result == [
        {"id": 1, "state": "EXECUTED"},
        {"id": 4, "state": "EXECUTED"},
    ], "Тест не пройден для состояния по умолчанию"


def test_filter_by_state_custom(input_data):
    """
    Тест проверяет работу функции с пользовательским параметром state.
    """
    result = filter_by_state(input_data, state="PENDING")
    assert result == [{"id": 2, "state": "PENDING"}], "Тест не пройден для пользовательского состояния"


def test_filter_by_state_empty(input_data):
    """
    Тест проверяет работу функции, когда нет операций с заданным состоянием.
    """
    result = filter_by_state(input_data, state="NON_EXISTENT")
    assert result == [], "Тест не пройден для несуществующего состояния"


def test_filter_by_state_invalid_input():
    """
    Тест проверяет поведение функции при некорректном входном списке.
    """
    with pytest.raises(TypeError):
        filter_by_state(None, state="EXECUTED")


# Данные для тестирования
test_dataa = [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

# Ожидаемый результат сортировки по возрастанию
expected_asc = [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

# Ожидаемый результат сортировки по убыванию
expected_desc = [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

# Параметризация теста с одним набором данных
@pytest.mark.parametrize("test_input, expected", [
    (test_dataa, expected_asc),
    (test_dataa, expected_desc)
])
def test_sort_by_date(test_input, expected):
    # Проверка сортировки
    assert sort_by_date(test_input, ascending=(expected == expected_asc)) == expected
