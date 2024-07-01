from typing import Any, Dict, List
from datetime import datetime



inform_state = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(origin_list: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Фильтрует список операций по заданному состоянию.

    Параметры:
        origin_list (List[Dict[str, Any]]): Список словарей, представляющих операции.
        state (str): Состояние, по которому нужно фильтровать операции. По умолчанию 'EXECUTED'.

    Возвращает:
        List[Dict[str, Any]]: Список отфильтрованных операций.
    """
    return [operation for operation in origin_list if operation.get("state") == state]


def sort_by_date(dict_list, ascending=True):
    # Конвертация строки даты в объект datetime для сравнения
    for d in dict_list:
        d['date'] = datetime.strptime(d['date'], '%Y-%m-%dT%H:%M:%S.%f')
    # Сортировка списка словарей по ключу 'date'
    sorted_list = sorted(dict_list, key=lambda x: x['date'], reverse=not ascending)
    # Конвертация объектов datetime обратно в строки
    for d in sorted_list:
        d['date'] = d['date'].strftime('%Y-%m-%dT%H:%M:%S.%f')  # Удаление последних трех цифр микросекунд
    return sorted_list


if __name__ == "__main__":
    print(
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    )
