import re
from collections import Counter


def filter_by_state(dict_list: list, state: str = "EXECUTED") -> list:
    """
    Принимает список словарей и возвращает отфильтрованный список по состоянию
    """
    filtered_list = []

    for item in dict_list:
        if item.get("state") == state:
            filtered_list.append(item)

    return filtered_list


def sort_by_date(dict_list: list, is_reversed: bool = True) -> list:
    """
    Принимает список словарей и возвращает отсортированный список по дате
    """
    return sorted(dict_list, reverse=is_reversed, key=lambda x: (x.get("date") is None, x.get("date")))


def process_bank_search(data: list, search: str) -> list[dict]:
    """Принимает список словарей и возвращает список отфильтрованный по заданным словам"""

    result = [item for item in data if re.search(search, item.get("description"), re.IGNORECASE)]

    return result


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """принимает список и возвращает словарь с количеством повторов категорий транзакций"""

    category_counts = Counter(transaction.get("description") for transaction in data)

    return {cat: category_counts.get(cat, 0) for cat in categories}
