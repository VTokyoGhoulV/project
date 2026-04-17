import pytest  # type: ignore


@pytest.fixture
def dict_list():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def combined_test_list():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 999000, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 999001, "state": "EXECUTED", "date": ""},
        {"id": 999002, "state": "CANCELED", "date": None},
        {"id": 999003, "state": "EXECUTED", "date": "2020-01-01"},
        {"id": 999004, "state": "CANCELED", "date": "31.12.2021T15:30:00.123456"},
        {"id": 999005, "state": "EXECUTED", "date": "2017-11-23 09:12:45.987654"},
        {"id": 999007, "state": "EXECUTED", "date": "not_a_date"},
        {"id": 999008, "state": "CANCELED", "date": "2019-02-29T10:10:10.101010"},
    ]
