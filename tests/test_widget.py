import pytest  # type: ignore

from src.widget import get_date, mask_account_card


# тесты функции mask_account_card
@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Visa Platinum 6831982476737658", "Visa Platinum 6831 98** **** 7658"),
    ],
)
def test_mask_account_card_valid(account_number, expected):
    assert mask_account_card(account_number) == expected


@pytest.mark.parametrize(
    "card_account_number, expected",
    [
        ("Visa 4779640000000000", "Visa 4779 64** **** 0000"),
        ("Master Card 5536680000000000", "Master Card 5536 68** **** 0000"),
        ("Счет 28954302521853252346", "Счет **2346"),
        ("Счет 2854724531296301234", "Счет **1234"),
        ("Счет 285472453129630123462", "Счет **3462"),
        ("Счет 2895 4302 52185 3252346", "Счет **2346"),
        ("Счет 289543d0252q18532E52346", "Некорректный номер счета"),
        ("Счет 28954%302521@85325$2346", "Некорректный номер счета"),
        ("", "Данные не введены"),
    ],
)
def test_mask_account_card(card_account_number, expected):
    assert mask_account_card(card_account_number) == expected


# тесты функции get_date
@pytest.mark.parametrize(
    "date, expected",
    [
        ("2020-07-07T10:30:59.24354", "07.07.2020"),
        ("2024-02-29", "29.02.2024"),
        ("29.02.2024", "29.02.2024"),
        ("2024/02/29", "29.02.2024"),
        ("01.01.0001", "01.01.0001"),
        ("31.12.9999", "31.12.9999"),
        ("2024_02_29", "29.02.2024"),
        ("", ""),
    ],
)
def test_get_date(date, expected):
    assert get_date(date) == expected
