import pytest  # type: ignore

from src.processing import filter_by_state, process_bank_operations, process_bank_search, sort_by_date

# тесты функции filter_by_state
by_state_default = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]
by_state_canceled = [
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


@pytest.mark.parametrize(
    "state, expected",
    [("EXECUTED", by_state_default), ("CANCELED", by_state_canceled), ("qwerty", [])],
)
def test_filter_by_state(dict_list, state, expected):
    assert filter_by_state(dict_list, state) == expected


@pytest.mark.parametrize("state, expected", [("EXECUTED", []), ("CANCELED", [])])
def test_filter_by_state_empty(state, expected):
    assert filter_by_state([], state) == expected


# тесты функции sort_by_date
by_date_default = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]
by_date_false = [
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
]


@pytest.mark.parametrize("is_reversed, expected", [(True, by_date_default), (False, by_date_false)])
def test_sort_by_date_reversed(dict_list, is_reversed, expected):
    assert sort_by_date(dict_list, is_reversed) == expected


by_date_duplicate = [
    {"id": 41428829, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
expected = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 41428829, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]


def test_sort_by_date_duplicate():
    assert sort_by_date(by_date_duplicate) == expected


expected_true = [
    {"id": 999002, "state": "CANCELED", "date": None},
    {"id": 999007, "state": "EXECUTED", "date": "not_a_date"},
    {"id": 999004, "state": "CANCELED", "date": "31.12.2021T15:30:00.123456"},
    {"id": 999003, "state": "EXECUTED", "date": "2020-01-01"},
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 999008, "state": "CANCELED", "date": "2019-02-29T10:10:10.101010"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 999000, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 999005, "state": "EXECUTED", "date": "2017-11-23 09:12:45.987654"},
    {"id": 999001, "state": "EXECUTED", "date": ""},
]
expected_false = [
    {"id": 999001, "state": "EXECUTED", "date": ""},
    {"id": 999005, "state": "EXECUTED", "date": "2017-11-23 09:12:45.987654"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 999000, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 999008, "state": "CANCELED", "date": "2019-02-29T10:10:10.101010"},
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 999003, "state": "EXECUTED", "date": "2020-01-01"},
    {"id": 999004, "state": "CANCELED", "date": "31.12.2021T15:30:00.123456"},
    {"id": 999007, "state": "EXECUTED", "date": "not_a_date"},
    {"id": 999002, "state": "CANCELED", "date": None},
]


def test_sort_by_date_with_none(combined_test_list):
    assert sort_by_date(combined_test_list) == expected_true


@pytest.mark.parametrize(
    "is_reversed, expected",
    [(True, expected_true), (False, expected_false)],
)
def test_sort_by_date_reversed_with_none(combined_test_list, is_reversed, expected):
    assert sort_by_date(combined_test_list, is_reversed) == expected


# Тесты для функции process_bank_operations


def test_count_single_category(transactions):
    """Тест: подсчёт одной существующей категории"""
    categories = ["Перевод организации"]
    result = process_bank_operations(transactions, categories)

    # "Перевод организации" встречается 2 раза
    assert result == {"Перевод организации": 2}


def test_count_multiple_categories(transactions):
    """Тест: подсчёт нескольких существующих категорий"""
    categories = ["Перевод организации", "Перевод со счета на счет"]
    result = process_bank_operations(transactions, categories)

    assert result == {"Перевод организации": 2, "Перевод со счета на счет": 2}


def test_category_not_exists(transactions):
    """Тест: категория, которой нет в транзакциях"""
    categories = ["Покупка в магазине"]
    result = process_bank_operations(transactions, categories)

    # Несуществующая категория должна вернуть 0
    assert result == {"Покупка в магазине": 0}


def test_mixed_categories(transactions):
    """Тест: смесь существующих и несуществующих категорий"""
    categories = ["Перевод организации", "Перевод с карты на карту", "Оплата услуг"]
    result = process_bank_operations(transactions, categories)

    assert result == {"Перевод организации": 2, "Перевод с карты на карту": 1, "Оплата услуг": 0}


def test_empty_categories_list(transactions):
    """Тест: пустой список категорий"""
    categories = []
    result = process_bank_operations(transactions, categories)

    assert result == {}


def test_empty_data_list(transactions):
    """Тест: пустой список транзакций"""
    categories = ["Перевод организации", "Перевод со счета на счет"]
    result = process_bank_operations([], categories)

    # При пустых данных все категории должны быть 0
    assert result == {"Перевод организации": 0, "Перевод со счета на счет": 0}


def test_case_sensitivity(transactions):
    """Тест: проверка чувствительности к регистру"""
    categories = ["перевод организации"]  # с маленькой буквы
    result = process_bank_operations(transactions, categories)

    # В данных "Перевод организации" (с большой буквы), поэтому должно быть 0
    assert result == {"перевод организации": 0}


def test_count_all_unique_descriptions(transactions):
    """Тест: подсчёт всех уникальных описаний"""
    categories = ["Перевод организации", "Перевод со счета на счет", "Перевод с карты на карту"]
    result = process_bank_operations(transactions, categories)

    assert result == {"Перевод организации": 2, "Перевод со счета на счет": 2, "Перевод с карты на карту": 1}


def test_duplicate_categories_in_input(transactions):
    """Тест: дубликаты категорий в списке для поиска"""
    categories = ["Перевод организации", "Перевод организации", "Перевод со счета на счет"]
    result = process_bank_operations(transactions, categories)

    # Функция должна корректно обработать дубликаты
    assert result == {"Перевод организации": 2, "Перевод со счета на счет": 2}


# Тесты для функции process_bank_search
def test_search_exact_phrase(transactions):
    """Тест поиска точной фразы"""
    result = process_bank_search(transactions, "Перевод организации")
    assert len(result) == 2
    assert result[0]["id"] == 939719570
    assert result[1]["id"] == 594226727
    assert all(item["description"] == "Перевод организации" for item in result)


def test_search_case_insensitive(transactions):
    """Тест регистронезависимого поиска"""
    result = process_bank_search(transactions, "перевод")
    assert len(result) == 5  # Все транзакции имеют слово "перевод"
    assert all("перевод" in item["description"].lower() for item in result)


def test_search_partial_match(transactions):
    """Тест поиска по части слова"""
    result = process_bank_search(transactions, "организ")
    assert len(result) == 2
    assert result[0]["id"] == 939719570
    assert result[1]["id"] == 594226727


def test_search_no_matches(transactions):
    """Тест когда совпадений нет"""
    result = process_bank_search(transactions, "несуществующая строка")
    assert len(result) == 0
    assert result == []
