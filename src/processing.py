from typing import Any


def filter_by_state(origin_list: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str]]:
    """Фунция, сортирующая список по ключу"""
    filtered_list = []
    for data in origin_list:
        if data.get("state") == state:
            filtered_list.append(data)
    return filtered_list


def sort_by_date(origin_list: list[dict[str, Any]], reverse_list: bool = True) -> list[dict[str, Any]]:
    """Функция для сортировки по доте в порядке убывания или возрастания"""
    sorted_list = sorted(origin_list, key=lambda d: d.get("date"), reverse=reverse_list)
