import json
import logging
import os

import pandas as pd


json_logger = logging.getLogger("utils_json_log")
json_logger.setLevel(logging.DEBUG)

csv_logger = logging.getLogger("utils_csv_log")
csv_logger.setLevel(logging.DEBUG)

xlsx_logger = logging.getLogger("utils_xlsx_log")
xlsx_logger.setLevel(logging.DEBUG)

file_logger = logging.getLogger("utils_file_log")
file_logger.setLevel(logging.DEBUG)

handler = logging.FileHandler("C:/Users/TokyoGhoul/PycharmProjects/project/logs/utils_log.log", "w", encoding="utf-8")

formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formater)

json_logger.addHandler(handler)
csv_logger.addHandler(handler)
xlsx_logger.addHandler(handler)
file_logger.addHandler(handler)


def file_check(file_path: str) -> bool:
    """Проверяет корректность файла для чтения и работы"""

    file_logger.info(f"Начало проверки файла. Путь до файла: {file_path}")

    if not os.path.exists(file_path):
        file_logger.warning("Файла не существует")  # Проверка существует ли файл
        print("Файла не существует")
        return False

    if os.path.getsize(file_path) == 0:
        file_logger.warning("Пустой файл")  # Проверка пустой ли файл
        print("Пустой файл")
        return False

    return True


def json_to_python(file_path: str) -> list:
    """Возвращает список словарей с данными транзакций из json файла"""

    json_logger.info(f"Начало перевода из json в python. Путь до файла: {file_path}")

    if file_check(file_path):
        with open(file_path, "r", encoding="utf-8") as json_file:

            try:  # Проверка на корректность JSON файла

                operations = json.load(json_file)

                if type(operations) is list:  # Проверка является ли содержимое файла списком
                    json_logger.info("Перевод из json в python")
                    return operations

                else:
                    json_logger.warning("Содержимое не является списком")
                    print("Содержимое не является списком")
                    return []

            except json.JSONDecodeError:
                json_logger.error("Ошибка! Файл содержит не корректный JSON")
                print("Ошибка! Файл содержит не корректный JSON")
                return []
    return []


def csv_to_python(file_path: str) -> list:
    """Возвращает список словарей с данными транзакций из csv файла"""

    csv_logger.info(f"Начало перевода из csv в python. Путь до файла: {file_path}")

    if file_check(file_path):

        csv_logger.info("Преобразование из csv в python")

        df = pd.read_csv(file_path, sep=";", encoding='utf-8') #type: ignore

        return df.to_dict(orient="records") # type: ignore[no-any-return]

    return []

def xlsx_to_python(file_path: str) -> list:
    """Возвращает список словарей с данными транзакций из xlsx файла"""

    xlsx_logger.info(f"Начало перевода из xlsx в python. Путь до файла: {file_path}")

    if file_check(file_path):

        xlsx_logger.info("Преобразование из xlsx в python")

        df = pd.read_excel(file_path)

        return df.to_dict(orient="records") # type: ignore[no-any-return]

    return []