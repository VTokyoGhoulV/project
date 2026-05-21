import json
from unittest.mock import mock_open, patch

import pandas as pd

from src.utils import csv_to_python, json_to_python, xlsx_to_python


# Тесты для функции json_to_python
def test_valid_json_list():

    mock_data = [{"id": 1, "name": "test"}]
    mock_json = json.dumps(mock_data)

    with patch("os.path.exists", return_value=True):
        with patch("os.path.getsize", return_value=1):
            with patch("builtins.open", mock_open(read_data=mock_json)):

                assert json_to_python("any_filename.json") == mock_data


def test_invalid_json_data():

    with patch("os.path.exists", return_value=True):
        with patch("os.path.getsize", return_value=1):
            with patch("builtins.open", mock_open(read_data="Не JSON формат")):

                assert json_to_python("any_filename.json") == []


def test_not_list_data():

    mock_data = {"id": 1, "name": "test"}
    mock_json = json.dumps(mock_data)

    with patch("os.path.exists", return_value=True):
        with patch("os.path.getsize", return_value=1):
            with patch("builtins.open", mock_open(read_data=mock_json)):

                assert json_to_python("any_filename.json") == []


def test_no_json_filet():

    with patch("os.path.exists", return_value=False):

        assert json_to_python("any_filename.json") == []


def test_empty_json_file():

    with patch("os.path.exists", return_value=True):
        with patch("os.path.getsize", return_value=0):

            assert json_to_python("any_filename.json") == []


# Тесты для функции csv_to_python
def test_valid_csv_list_real(temp_csv_file):

    csv_content = "id;name;amount\n1;test;100\n2;test2;200"
    temp_csv_file.write_text(csv_content, encoding="utf-8")

    result = csv_to_python(str(temp_csv_file))

    expected_result = [{"id": 1, "name": "test", "amount": 100}, {"id": 2, "name": "test2", "amount": 200}]
    assert result == expected_result


def test_empty_csv_file_real(temp_csv_file):

    temp_csv_file.write_text("", encoding="utf-8")

    result = csv_to_python(str(temp_csv_file))
    assert result == []


def test_csv_only_headers_real(temp_csv_file):

    csv_content = "id;name;amount"
    temp_csv_file.write_text(csv_content, encoding="utf-8")

    result = csv_to_python(str(temp_csv_file))
    assert result == []


def test_csv_file_not_found():

    result = csv_to_python("non_existent_file.csv")
    assert result == []


# Тесты для функции xlsx_to_python
def test_valid_xlsx_list(temp_xlsx_file):

    test_data = {"id": [1, 2], "name": ["test1", "test2"], "amount": [100, 200]}
    df_expected = pd.DataFrame(test_data)
    expected_result = df_expected.to_dict(orient="records")

    df_expected.to_excel(temp_xlsx_file, index=False)

    result = xlsx_to_python(str(temp_xlsx_file))
    assert result == expected_result


def test_empty_xlsx_file(temp_xlsx_file):

    df_empty = pd.DataFrame()
    df_empty.to_excel(temp_xlsx_file, index=False)

    result = xlsx_to_python(str(temp_xlsx_file))
    assert result == []


def test_no_xlsx_file():

    result = xlsx_to_python("non_existent_file.xlsx")
    assert result == []
