def get_mask_card_number(card_number: int) -> str:
    """
    Принимает на вход номер карты в виде числа и возвращает маску номера.
    """
    masked_card_number = ""
    str_card_number = str(card_number).replace(" ", "")

    for index, char in enumerate(str_card_number):
        if index % 4 == 0 and index != 0:
            masked_card_number += " "

        if 5 < index < len(str_card_number) - 4:
            masked_card_number += "*"

        else:
            masked_card_number += char

    return masked_card_number


def get_mask_account(account_number: int) -> str:
    """
    Принимает на вход номер счета в виде числа и возвращает маску номера.
    """
    masked_account_number = "**"
    if len(str(account_number)) == 20:
        for index, char in enumerate(str(account_number)):
            if index >= len(str(account_number)) - 4:
                masked_account_number += char
    else:
        return "Некорректный номер счета"

    return masked_account_number
