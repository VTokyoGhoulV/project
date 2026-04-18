import pytest  # type: ignore

from src.processing import filter_by_state, sort_by_date

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
