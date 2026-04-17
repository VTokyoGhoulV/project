from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card_number: str) -> str:
    """
    Принимает на вход номер счета или карты в и возвращает маску номера.
    """

    if len(account_card_number) > 0:
        if "Счет" in account_card_number:
            parts = account_card_number.split(" ", 1)
            account_name = parts[0]
            account_number = parts[1]
            spaceless_account_number = account_number.replace(" ", "")

            if len(spaceless_account_number) == 20:

                masked_account_number = get_mask_account(int(spaceless_account_number))

                return f"{account_name} {masked_account_number}"
            else:
                return "Некорректный номер счета"

        else:
            parts = account_card_number.rsplit(" ", 1)
            card_name = parts[0]
            card_number = parts[1]

            masked_card_number = get_mask_card_number(int(card_number))

            return f"{card_name} {masked_card_number}"
    else:
        return "Данные не введены"


def get_date(date: str) -> str:
    """
    Изменяет дату в формате YYYY-MM-DDTHH:MM:SS.MS в формат DD.MM.YYYY
    """

    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"
