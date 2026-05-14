import json
import os


def json_to_python(file_path: str) -> list:
    """ Возвращает список словарей с данными транзакций из json файла"""

    if not os.path.exists(file_path):  # Проверка существует ли файл
        print("Файла не существует")
        return []

    if os.path.getsize(file_path) == 0:  # Проверка пустой ли файл
        print("Пустой файл")
        return []

    with open(file_path, "r", encoding="utf-8") as json_file:

        try:  # Проверка на корректность JSON файла

            operations = json.load(json_file)

            if type(operations) is list:  # Проверка является ли содержимое файла списком
                return operations

            else:
                print("Содержимое не является списком")
                return []

        except json.JSONDecodeError:

            print("Ошибка! Файл содержит не корректный JSON")
            return []
