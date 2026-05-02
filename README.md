# Банковские операции

![Python](https://img.shields.io/badge/Python-3.13+-blue)
![Pytest](https://img.shields.io/badge/tests-pytest-green)
![Poetry](https://img.shields.io/badge/package_manager-poetry-purple)
![Status](https://img.shields.io/badge/status-learning_project-orange)

Учебный Python-проект для обработки банковских транзакций: маскирования номеров карт и счетов, форматирования дат, фильтрации и сортировки операций, работы с генераторами и логирования вызовов функций.

## Оглавление

- [Возможности](#возможности)
- [Структура проекта](#структура-проекта)
- [Установка](#установка)
- [Использование](#использование)
- [Тестирование и качество кода](#тестирование-и-качество-кода)
- [Требования](#требования)

## Возможности

- Маскирование номеров банковских карт и счетов.
- Форматирование дат из ISO-строк и коротких дат в формат `ДД.ММ.ГГГГ`.
- Фильтрация операций по статусу и сортировка по дате.
- Фильтрация транзакций по валюте.
- Получение описаний транзакций через генератор.
- Генерация номеров карт в формате `XXXX XXXX XXXX XXXX`.
- Логирование результата или ошибки выполнения функции в консоль или файл.

## Структура проекта

```text
.
├── src/
│   ├── __init__.py
│   ├── decorators.py
│   ├── generators.py
│   ├── masks.py
│   ├── processing.py
│   └── widget.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_decorators.py
│   ├── test_generator.py
│   ├── test_masks.py
│   ├── test_processing.py
│   └── test_widget.py
├── pyproject.toml
├── poetry.lock
└── README.md
```

## Установка

Склонируйте репозиторий и перейдите в директорию проекта:

```bash
git clone <URL_репозитория>
cd project
```

Установите зависимости через Poetry:

```bash
poetry install --with dev,lint
```

Активируйте виртуальное окружение:

```bash
poetry shell
```

## Использование

### Маскирование карт и счетов

```python
from src.masks import get_mask_account, get_mask_card_number

print(get_mask_card_number(1234567812345678))
# 1234 56** **** 5678

print(get_mask_account(12345678901234567890))
# **7890
```

### Маскирование строки с названием карты или счета

```python
from src.widget import mask_account_card

print(mask_account_card("Visa Platinum 1234567812345678"))
# Visa Platinum 1234 56** **** 5678

print(mask_account_card("Счет 12345678901234567890"))
# Счет **7890
```

### Форматирование даты

```python
from src.widget import get_date

print(get_date("2024-03-11T02:26:18.671407"))
# 11.03.2024

print(get_date("2024-03-11"))
# 11.03.2024
```

### Фильтрация и сортировка операций

```python
from src.processing import filter_by_state, sort_by_date

operations = [
    {"state": "EXECUTED", "date": "2024-01-01"},
    {"state": "CANCELED", "date": "2023-01-01"},
]

print(filter_by_state(operations))
print(sort_by_date(operations))
```

### Генераторы

```python
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

transactions = [
    {
        "operationAmount": {
            "currency": {"code": "USD"},
        },
        "description": "Перевод организации",
    }
]

print(list(filter_by_currency(transactions, "USD")))
print(list(transaction_descriptions(transactions)))
print(list(card_number_generator(1, 3)))
# ['0000 0000 0000 0001', '0000 0000 0000 0002', '0000 0000 0000 0003']
```

### Логирование

```python
from src.decorators import log


@log()
def add_numbers(first: int, second: int) -> int:
    return first + second


@log("log.log")
def divide_numbers(first: int, second: int) -> float:
    return first / second


add_numbers(2, 3)
divide_numbers(10, 2)
```

Декоратор `log` записывает имя функции, статус выполнения, результат или ошибку, входные данные и время начала/окончания вызова.

## Тестирование и качество кода

Запуск тестов:

```bash
poetry run pytest
```

Запуск тестов с отчетом о покрытии:

```bash
poetry run pytest --cov=src --cov-report=term-missing
```

Проверка стиля и типов:

```bash
poetry run flake8 src tests
poetry run mypy src
poetry run black --check src tests
poetry run isort --check-only src tests
```

## Требования

- Python 3.13+
- Poetry
- pytest для запуска тестов
- flake8, mypy, black и isort для проверок качества кода

## Автор

VTokyoGhoulV
