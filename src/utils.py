import json
import os
import logging


logger = logging.getLogger("utils_log")
logger.setLevel(logging.INFO)
handler = logging.FileHandler("logs/utils_log.log", "w", encoding="utf-8")
formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formater)
logger.addHandler(handler)

def json_to_python(file_path: str) -> list:
    """Возвращает список словарей с данными транзакций из json файла"""

    logger.info("Начало перевода из json в python")
    if not os.path.exists(file_path):
        logger.warning("Файла не существует")# Проверка существует ли файл
        print("Файла не существует")
        return []

    if os.path.getsize(file_path) == 0:
        logger.warning("Пустой файл")# Проверка пустой ли файл
        print("Пустой файл")
        return []

    with open(file_path, "r", encoding="utf-8") as json_file:

        try:  # Проверка на корректность JSON файла

            operations = json.load(json_file)

            if type(operations) is list:  # Проверка является ли содержимое файла списком
                logger.info("Перевод из json в python")
                return operations

            else:
                logger.warning("Содержимое не является списком")
                print("Содержимое не является списком")
                return []

        except json.JSONDecodeError:
            logger.error("Ошибка! Файл содержит не корректный JSON")
            print("Ошибка! Файл содержит не корректный JSON")
            return []
