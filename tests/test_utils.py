from unittest import TestCase, mock
from src.utils import read_transactions
from unittest import TestCase, mock
from src.external_api import convert_currency


class TestUtils(TestCase):
    @mock.patch('src.utils.open', mock.mock_open(read_data='[{"amount": 100}]'))
    def test_read_transactions(self):
        result = read_transactions('fake_path')
        self.assertEqual(result, [{"amount": 100}])


class TestExternalAPI(TestCase):
    @mock.patch('src.external_api.requests.get')
    def test_convert_currency(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'result': 7400.0}
        result = convert_currency(100, 'USD')
        self.assertEqual(result, 7400.0)
