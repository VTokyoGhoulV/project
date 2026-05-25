import pandas as pd

from generators import filter_by_currency
from src.processing import filter_by_state, process_bank_search, sort_by_date
from src.utils import csv_to_python, json_to_python, xlsx_to_python
from widget import get_date, mask_account_card

if __name__ == "__main__":
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберете необходимый пункт в меню:")
    print("1. Получить информацию из файла JSON")
    print("2. Получить информацию из файла CSV")
    print("3. Получить информацию из файла XLSX")

    while True:

        file_choose = input("Введите номер: ")

        if file_choose == "1":
            transactions = json_to_python("C:/Users/TokyoGhoul/PycharmProjects/project/data/operations.json")
            print("Для обработки выбран JSON файл")
            break

        elif file_choose == "2":
            transactions = csv_to_python("C:/Users/TokyoGhoul/PycharmProjects/project/data/transactions.csv")
            print("Для обработки выбран CSV файл")
            break

        elif file_choose == "3":
            transactions = xlsx_to_python("C:/Users/TokyoGhoul/PycharmProjects/project/data/transactions_excel.xlsx")
            print("Для обработки выбран XLSX файл")
            break

        else:
            print("Некорректный ввод\n")

    print("\nВведите статус, по которому необходимо выполнить фильтрацию.")

    while True:

        user_choose = input("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING: ").upper()

        if user_choose == "EXECUTED":
            transactions = filter_by_state(transactions, "EXECUTED")
            print("Операции отфильтрованы по статусу \"EXECUTED\"")
            break

        elif user_choose == "CANCELED":
            transactions = filter_by_state(transactions, "CANCELED")
            print("Операции отфильтрованы по статусу \"CANCELED\"")
            break

        elif user_choose == "PENDING":
            transactions = filter_by_state(transactions, "PENDING")
            print("Операции отфильтрованы по статусу \"PENDING\"")
            break

        else:
            print(f"Статус операции {user_choose} не существует")

    print("\nОтсортировать операции по дате? Да/Нет")
    user_input = input().capitalize()

    if user_input == "Да":
        transactions = sort_by_date(transactions)

    print("\nВыводить только рублевые транзакции? Да/Нет")
    user_input = input().capitalize()

    if user_input == "Да":
        transactions = list(filter_by_currency(transactions, "RUB"))

    print("\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет")
    user_input = input().capitalize()

    if user_input == "Да":

        search = input("\nВведите слово: ")
        transactions = process_bank_search(transactions, search)

    if transactions:
        print("\nРаспечатываю итоговый список транзакций...")
        print(f"\nВсего банковских операций в выборке: {len(transactions)}\n")

        for transaction in transactions:

            print(f"{get_date(transaction["date"])} {transaction["description"]}")

            if transaction.get("from") and pd.notna(transaction.get("from")) and transaction.get("to"):
                print(f"{mask_account_card(transaction['from'])} -> {mask_account_card(transaction['to'])}")
            else:
                print(f"{mask_account_card(transaction['to'])}")

            if file_choose == "1":
                print(
                    f"Сумма: {transaction["operationAmount"]["amount"]} "
                    f"{transaction["operationAmount"]["currency"]["name"]}"
                )
            else:
                print(f"Сумма: {transaction["amount"]} {transaction["currency_name"]}")

            print()

    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
