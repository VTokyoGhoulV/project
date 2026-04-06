def get_mask_card_number(card_number: int) -> str:
    """
    Принимает на вход номер карты в виде числа и возвращает маску номера.
    """
    masked_card_number = ""
    for index, char in enumerate(str(card_number)):
        if index % 4 == 0 and index != 0:
            masked_card_number += " "

        if index > 5 and index < len(str(card_number)) - 4:
            masked_card_number += "*"

        else:
            masked_card_number += char

    return masked_card_number


def get_mask_account(account_number: int) -> str:
    """
    Принимает на вход номер счета в виде числа и возвращает маску номера.
    """
    masked_account_number = "**"
    for index, char in enumerate(str(account_number)):
        if index >= len(str(account_number)) - 4:
            masked_account_number += char

    return masked_account_number
