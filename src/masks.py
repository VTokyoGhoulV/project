import logging

logger = logging.getLogger("masks_log")
logger.setLevel(logging.INFO)
handler = logging.FileHandler("logs/masks_log.log", "w", encoding="utf-8")
formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formater)
logger.addHandler(handler)

def get_mask_card_number(card_number: int) -> str:
    """
    Принимает на вход номер карты в виде числа и возвращает маску номера.
    """
    logger.info(f"Начало маскирования номера карты. Номер карты: {card_number}")
    masked_card_number = ""
    str_card_number = str(card_number).replace(" ", "")

    for index, char in enumerate(str_card_number):
        if index % 4 == 0 and index != 0:
            masked_card_number += " "

        if 5 < index < len(str_card_number) - 4:
            masked_card_number += "*"

        else:
            masked_card_number += char

    logger.info(f"Маскированный номер карты: {masked_card_number}")
    return masked_card_number


def get_mask_account(account_number: int) -> str:
    """
    Принимает на вход номер счета в виде числа и возвращает маску номера.
    """
    logger.info(f"Начало маскировки номера счета. Номер счета: {account_number}")
    masked_account_number = "**"
    if len(str(account_number)) == 20:
        for index, char in enumerate(str(account_number)):
            if index >= len(str(account_number)) - 4:
                masked_account_number += char
    else:
        logger.warning("Некорректный номер счета")
        return "Некорректный номер счета"

    logger.info(f"Маскированный номер счета: {masked_account_number}")
    return masked_account_number
