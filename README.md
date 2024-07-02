# Учебный проект по Python
## Описание

Данный проект выполнен в целях практики написания кода на языке Python. Файл содержит функции для скрытия номера банковской карты и счета.

## Установка

1. Клонируйте репозиторий:
```
git clone https://github.com/Zelu141/HW
```
## Пример использования функции filter_by_state
```python
operations = [
    {'id': 1, 'state': 'EXECUTED'},
    {'id': 2, 'state': 'PENDING'}
]

filtered_operations = filter_by_state(operations)
print(filtered_operations)
```
## Примеры использования функций :

### Фильтрация транзакций по валюте

```python
from src.generators import filter_by_currency

transactions = [Место для ваших транзакций] 
filtered_transactions = list(filter_by_currency(transactions, 'USD'))
```

## Тестирование

Для запуска тестов в этом проекте используется библиотека `pytest`. Убедитесь, что она установлена в вашем виртуальном окружении. Если она ещё не установлена, вы можете установить её с помощью следующей команды:
````commandline
poetry add --group dev pytest
````

### Запуск тестов

Чтобы запустить все тесты, выполните следующую команду в терминале:
```commandline
pytest
```

### Описание тестов

В проекте представлены следующие тесты для функции `filter_by_state`:

- `test_filter_by_state_default`: Проверяет фильтрацию операций с состоянием по умолчанию (`EXECUTED`).
- `test_filter_by_state_custom`: Проверяет фильтрацию операций с пользовательским состоянием (`PENDING`).
- `test_filter_by_state_empty`: Проверяет поведение функции при отсутствии операций с заданным состоянием.
- `test_filter_by_state_invalid_input`: Проверяет обработку функцией некорректного входного списка.

## Контакты
Контакты для обратной связи:[kolenskiypython@gmail.com](mailto:kolenskiypython@gmail.com)