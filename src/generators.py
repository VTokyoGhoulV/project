from typing import Iterator


def filter_by_currency(transactions: list, currency: str) -> Iterator:
    """Фильтрует список транзакций по валюте"""
    for transaction in transactions:
        try:
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction
        except (KeyError, TypeError, LookupError):
            continue


def transaction_descriptions(transactions: list) -> Iterator:
    """Возвращает описание транзакции"""
    for item in transactions:
        yield item["description"]


def card_number_generator(start: int, end: int) -> Iterator:
    """Генерирует номера карт в формате XXXX XXXX XXXX XXXX"""
    real_start = max(start, 1)
    real_end = min(end, 9999999999999999)
    final_number_in_card = real_start

    while final_number_in_card <= real_end:
        if final_number_in_card <= 9999999999999999:
            card_number = str(final_number_in_card).zfill(16)
        else:
            return

        yield " ".join(card_number[i : i + 4] for i in range(0, 16, 4))
        final_number_in_card += 1
