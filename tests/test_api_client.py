import requests
import unittest
import unittest.mock
from unittest.mock import patch
from src.api_client import get_location

class ApiClientTest(unittest.TestCase):

    @patch('src.api_client.requests.get')
    def test_get_location_returns_expected_data(self, mock_get):
        # import ipdb; ipdb.set_trace()
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
        'countryName': 'USA',
        'cityName': 'FLORIDA',
        'regionName': 'MIAMI',
        }

        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"), "USA")
        self.assertEqual(result.get("region"), "MIAMI")
        self.assertEqual(result.get("city"), "FLORIDA")

        mock_get.assert_called_once_with("https://freeipapi.com/api/json/8.8.8.8")

    # Test with side effect
    @patch('src.api_client.requests.get')
    def test_get_location_returns_side_effect(self, mock_get):
        # import ipdb; ipdb.set_trace()
        mock_get.side_effect = [
            requests.exceptions.RequestException("Service Unavailable"),
            unittest.mock.Mock(
                status_code = 200,
                json = lambda: {
                    'countryName': 'USA',
                    'cityName': 'FLORIDA',
                    'regionName': 'MIAMI',
                }
            )
        ]
        # Case Error
        with self.assertRaises(requests.exceptions.RequestException):
            get_location("8.8.8.8")

        # Success Case
        result = get_location("8.8.8.8")

        self.assertEqual(result.get("country"), "USA")
        self.assertEqual(result.get("region"), "MIAMI")
        self.assertEqual(result.get("city"), "FLORIDA")

        