import os

import pytest  # type: ignore

from src.decorators import log


# Тесты декоратора log
# Тесты на возврат
@pytest.mark.parametrize("file_name, expected", [(None, "Test"), ("log.log", "Test")])
def test_log_return(file_name, expected):
    @log(file_name)
    def test_function():
        return "Test"

    assert test_function() == expected


# Тесты логирования успешных функций
def test_successful_function_logs_to_console(capsys):
    @log()
    def test_function():
        return "Test"

    test_function()
    captured = capsys.readouterr()

    assert "FuncName: test_function. Status: ok." in captured.out
    assert "Output: Test" in captured.out
    assert "Start:" in captured.out
    assert "End:" in captured.out


def test_successful_function_logs_to_file():
    @log("log.log")
    def test_function():
        return "Test"

    test_function()

    with open(os.path.join(os.getcwd(), "log.log"), "r") as f:
        file = f.read()
    assert "FuncName: test_function. Status: ok." in file
    assert "Output: Test" in file
    assert "Start:" in file
    assert "End:" in file


# Тесты логирования ошибок
def test_error_handling_to_console(capsys):

    @log()
    def divide_numbers(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide_numbers(10, 0)

    captured = capsys.readouterr()
    assert "FuncName: divide_numbers. Error: ZeroDivisionError:" in captured.out
    assert "Inputs: (10, 0), {}" in captured.out
    assert "Start:" in captured.out
    assert "End:" in captured.out


def test_error_handling_to_file():

    @log("log.log")
    def divide_numbers(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide_numbers(10, 0)

    with open(os.path.join(os.getcwd(), "log.log"), "r") as f:
        file = f.read()
    assert "FuncName: divide_numbers. Error: ZeroDivisionError:" in file
    assert "Inputs: (10, 0), {}" in file
    assert "Start:" in file
    assert "End:" in file
