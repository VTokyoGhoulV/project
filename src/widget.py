from masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card_number: str) -> str:
    if "Счет" in account_card_number:
        parts = account_card_number.rsplit(" ", 1)
        account_name = parts[0]
        account_number = parts[1]

        masked_account_number = get_mask_account(int(account_number))

        return f"{account_name} {masked_account_number}"

    else:
        parts = account_card_number.rsplit(" ", 1)
        card_name = parts[0]
        card_number = parts[1]

        masked_card_number = get_mask_card_number(int(card_number))

        return f"{card_name} {masked_card_number}"


print(mask_account_card("Счет 73654108430135874305"))
