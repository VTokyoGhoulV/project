from unittest.mock import patch

from src.external_api import exchange_currency


@patch("requests.get")
def test_exchange_currency_usd(mock_get):
    mock_get.return_value.json.return_value = {"result": 123.45}

    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}
    assert exchange_currency(transaction) == 123.45
    mock_get.assert_called_once()


def test_exchange_currency_rub():

    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "RUB"}}}
    assert exchange_currency(transaction) == 100

@patch("requests.get")
def test_exchange_currency_none(mock_get):
    mock_get.return_value.json.return_value = {}

    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}
    assert exchange_currency(transaction) is None
    mock_get.assert_called_once()