import json
import os


def json_to_python(file_path: str) -> list:

    if not os.path.exists(file_path):
        print("Файла не существует")  # Проверка существует ли файл
        return []

    if os.path.getsize(file_path) == 0:
        print("Пустой файл")  # Проверка пустой ли файл
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

            print("Ошибка! Файл содержить не корректный JSON")
            return []
