# 🏦 Банковские операции --- обработка и анализ

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Pytest](https://img.shields.io/badge/tests-pytest-green)
![Status](https://img.shields.io/badge/status-learning_project-orange)

------------------------------------------------------------------------

## 📚 Оглавление

-   [Описание проекта](#описание-проекта)
-   [Структура проекта](#структура-проекта)
-   [Установка](#установка)
-   [Использование](#использование)
-   [Генераторы](#генераторы)
-   [Тестирование](#тестирование)
-   [Требования](#требования)

------------------------------------------------------------------------

## 📌 Описание проекта

Проект предназначен для обработки банковских транзакций.

Функциональность: - маскирование карт и счетов; - форматирование
данных; - фильтрация и сортировка операций; - генераторы для обработки
потоков данных.

------------------------------------------------------------------------

## 🗂 Структура проекта

``` bash
src/
├── masks.py
├── widget.py
├── processing.py
├── generators.py

tests/
├── test_masks.py
├── test_widget.py
├── test_processing.py
├── test_generator.py
└── conftest.py
```

------------------------------------------------------------------------

## ⚙️ Установка

``` bash
git clone <URL_репозитория>
cd <имя_проекта>
pip install -r requirements.txt
```

------------------------------------------------------------------------

## 🚀 Использование

### 🔐 Маскирование

``` python
from src.masks import get_mask_card_number, get_mask_account

print(get_mask_card_number("1234567812345678"))
print(get_mask_account("12345678901234567890"))
```

------------------------------------------------------------------------

### 🧾 Форматирование

``` python
from src.widget import mask_account_card, get_date

print(mask_account_card("Visa Platinum 1234567812345678"))
print(get_date("2024-03-11T02:26:18.671407"))
```

------------------------------------------------------------------------

### 📊 Фильтрация и сортировка

``` python
from src.processing import filter_by_state, sort_by_date

data = [
    {"state": "EXECUTED", "date": "2024-01-01"},
    {"state": "CANCELED", "date": "2023-01-01"},
]

print(filter_by_state(data))
print(sort_by_date(data))
```

------------------------------------------------------------------------

## 🔁 Генераторы

### 💱 Фильтрация по валюте

``` python
from src.generators import filter_by_currency

for t in filter_by_currency(transactions, "USD"):
    print(t)
```

------------------------------------------------------------------------

### 📝 Описания транзакций

``` python
from src.generators import transaction_descriptions

for desc in transaction_descriptions(transactions):
    print(desc)
```

------------------------------------------------------------------------

### 💳 Генерация номеров карт

``` python
from src.generators import card_number_generator

for card in card_number_generator(1, 3):
    print(card)
```

------------------------------------------------------------------------

## 🧪 Тестирование

``` bash
pytest
```

Что покрыто: - маскирование; - форматирование; - сортировка; -
генераторы; - граничные случаи.

------------------------------------------------------------------------

## 📦 Требования

-   Python 3.10+
-   pytest

------------------------------------------------------------------------

## 👨‍💻 Автор

Учебный проект
