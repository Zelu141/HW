from typing import Any, Dict, List


def filter_by_state(origin_list: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Фильтрует список операций по заданному состоянию.

    Параметры:
        origin_list (List[Dict[str, Any]]): Список словарей, представляющих операции.
        state (str): Состояние, по которому нужно фильтровать операции. По умолчанию 'EXECUTED'.

    Возвращает:
        List[Dict[str, Any]]: Список отфильтрованных операций.
    """
    return [operation for operation in origin_list if operation.get('state') == state]


def sort_by_date(origin_list: List[Dict[str, Any]], reverse_list: bool = True) -> List[Dict[str, Any]]:
    """Функция для сортировки по доте в порядке убывания или возрастания"""
    sorted_list = sorted(origin_list, key=lambda d: d["date"], reverse=reverse_list)
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
