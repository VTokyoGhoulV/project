from unittest.mock import patch
import requests
import pytest
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
def test_exchange_currency_checks_url_and_headers(mock_get):
    # Настраиваем мок
    mock_get.return_value.json.return_value = {"result": 97.50}

    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "USD"}
        }
    }

    # Вызываем функцию
    exchange_currency(transaction)

    # Проверяем, что requests.get был вызван с правильными параметрами
    mock_get.assert_called_once()

    # Получаем аргументы вызова
    call_args = mock_get.call_args
    url = call_args[0][0]  # первый позиционный аргумент - URL
    headers = call_args[1]["headers"]  # аргумент headers из kwargs

    # Проверяем URL
    assert "to=RUB" in url
    assert "from=USD" in url
    assert "amount=100" in url
    assert "https://api.apilayer.com/exchangerates_data/convert" in url

    # Проверяем заголовки
    assert "apikey" in headers
    assert headers["apikey"] != ""  # ключ не пустой (если установлен в .env)

@patch("requests.get")
def test_exchange_currency_handles_connection_error(mock_get):
    # Мокируем исключение при вызове requests.get
    mock_get.side_effect = requests.exceptions.ConnectionError("Нет соединения")

    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "USD"}
        }
    }

    # Ожидаем, что функция выбросит исключение
    with pytest.raises(requests.exceptions.ConnectionError):
        exchange_currency(transaction)


@patch("requests.get")
def test_exchange_currency_handles_timeout(mock_get):
    mock_get.side_effect = requests.exceptions.Timeout("Таймаут")

    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "USD"}
        }
    }

    with pytest.raises(requests.exceptions.Timeout):
        exchange_currency(transaction)


@patch("requests.get")
def test_exchange_currency_handles_missing_result_field(mock_get):
    # API вернул JSON без поля "result"
    mock_get.return_value.json.return_value = {"error": "Invalid currency code"}

    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "XXX"}  # несуществующая валюта
        }
    }

    # Ожидаем KeyError или возврат None (зависит от реализации)
    assert exchange_currency(transaction) is None


@patch("requests.get")
def test_exchange_currency_handles_http_error(mock_get):
    # Создаём мок-ответ с ошибкой
    mock_response = mock_get.return_value
    mock_response.status_code = 404
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Not Found")
    # Если ваш код вызывает raise_for_status()
    # Если нет - просто возвращаем пустой JSON с ошибкой
    mock_response.json.return_value = {"error": "Not found"}

    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "USD"}
        }
    }

    # Функция должна корректно обработать ошибку
    # Например, вернуть None или выбросить исключение
    result = exchange_currency(transaction)

    # Проверяем, что функция обработала ошибку (зависит от реализации)
    # Если функция не обрабатывает - ожидаем исключение
    assert result is None  # или проверка на исключение