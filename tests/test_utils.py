import unittest
from src.utils import read_transactions


class TestUtils(unittest.TestCase):
    def test_read_transactions_valid(self):
        # Тест на чтение валидного файла
        transactions = read_transactions('data.operations.json')
        self.assertIsInstance(transactions, list)
        self.assertGreater(len(transactions), 0)

    def test_read_transactions_empty(self):
        # Тест на чтение пустого файла
        transactions = read_transactions('data.empty.json')
        self.assertEqual(transactions, [])

    def test_read_transactions_not_found(self):
        # Тест на чтение несуществующего файла
        transactions = read_transactions('data.not_found.json')
        self.assertEqual(transactions, [])
