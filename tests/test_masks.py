import pytest

from src.masks import get_mask_account, get_mask_card_number


# тесты для функции get_mask_card_number
def test_get_mask_card_number_valid():
    assert get_mask_card_number("6831982476737658") == "6831 98** **** 7658"


def test_get_mask_card_number_empty():
    assert get_mask_card_number("") == ""


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("4111 1111 1111 1111", "4111 11** **** 1111"),
        ("5555555555554444", "5555 55** **** 4444"),
        ("378282246310005", "3782 82** *** 0005"),
        ("30000000000004", "3000 00** **** 0004"),
        ("6011000000000004", "6011 00** **** 0004"),
        ("6759411100000008", "6759 41** **** 0008"),
        ("586824160825533338", "5868 24** **** 3338"),
    ],
)
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


# тесты для функции get_mask_account
def test_get_mask_account_valid():
    assert get_mask_account("73654108430135874305") == "**4305"


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("736541084301358743", "Некорректный номер счета"),
        ("7365410843013587430552", "Некорректный номер счета"),
    ],
)
def test_get_mask_account_not_valid(account_number, expected):
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("11111111111111111111", "**1111"),
        ("4081781010000000000", "Некорректный номер счета"),
        ("408178101000000000000", "Некорректный номер счета"),
        ("", "Некорректный номер счета"),
    ],
)
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected
