import os
from collections.abc import MutableMapping

import requests
from dotenv import load_dotenv


def exchange_currency(transaction: dict) -> float | None:
    """ Выдает сумму транзакции, обращается на сайт для конвертации валют при необходимости """

    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])

    else:

        load_dotenv()
        rub_currency = "RUB"
        original_currency = transaction["operationAmount"]["currency"]["code"]
        amount = transaction["operationAmount"]["amount"]
        url = (
            f"https://api.apilayer.com/exchangerates_data/convert?"
            f"to={rub_currency}&from={original_currency}&amount={amount}"
        )

        headers: MutableMapping[str, str | bytes] = {}
        api_key = os.getenv("API_KEY")
        if api_key is not None:
            headers["apikey"] = api_key

        convert_requests = requests.get(url, headers=headers).json()
        converted_currency = convert_requests.get("result")
        if converted_currency:
            return float(converted_currency)
        else:
            return None
