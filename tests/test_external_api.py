from unittest import TestCase, mock

from src.external_api import convert_to_rub


class TestExternalAPI(TestCase):
    @mock.patch('src.external_api.requests.get')
    def test_convert_to_rub_success(self, mock_get):
        # Настройка мока для успешного ответа API
        mock_response = mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'result': 74.0}
        mock_get.return_value = mock_response

        # Проверка конвертации USD в RUB
        result = convert_to_rub(1, 'USD')
        self.assertEqual(result, 74.0)
    @mock.patch('src.external_api.requests.get')
    def test_convert_to_rub_failure(self, mock_get):
        # Настройка мока для неудачного ответа API
        mock_response = mock.Mock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        # Проверка обработки ошибки API
        with self.assertRaises(Exception):
            convert_to_rub(1, 'USD')

    @mock.patch('src.external_api.requests.get')
    def test_convert_to_rub_invalid_currency(self, mock_get):
        # Настройка мока для невалидной валюты
        mock_response = mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'result': None}
        mock_get.return_value = mock_response

        # Проверка конвертации при невалидной валюте
        result = convert_to_rub(1, 'XXX')
