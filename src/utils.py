import json
from typing import Dict, List


def read_transactions(file_path: str) -> List[Dict]:
    """
       Читает данные о финансовых транзакциях из JSON-файла.

        file_path: Путь к файлу с данными о транзакциях.
       return: Список словарей с данными о транзакциях или пустой список,
                если файл пустой, содержит не список или не найден.
       """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            transactions = json.load(file)
            if isinstance(transactions, list):
                return transactions
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
