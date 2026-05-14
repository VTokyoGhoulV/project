import json
from unittest.mock import mock_open, patch

from src.utils import json_to_python


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
