import datetime
from functools import wraps


# Декоратор создающий лог
def log(file_name: None | str = None):  # type: ignore
    """
    Создает лог по работе функции
    """

    def wrapper(func):  # type: ignore

        @wraps(func)
        def inner(*args, **kwargs):  # type: ignore

            start_str = datetime.datetime.now()

            try:

                result = func(*args, **kwargs)
                end_str = datetime.datetime.now()
                log_message = (
                    f"FuncName: {func.__name__}. Status: ok. Output: {result}. Start: {start_str} End: {end_str}\n"
                )

                if file_name:
                    with open(file_name, "a", encoding="utf-8") as file:
                        file.write(log_message)

                else:
                    print(log_message)

                return result

            except Exception as e:

                end_str = datetime.datetime.now()

                log_error_message = (
                    f"FuncName: {func.__name__}. Error: {type(e).__name__}: {e}. "
                    f"Inputs: {args}, {kwargs} Start: {start_str} End: {end_str}\n"
                )

                if file_name:
                    with open(file_name, "a", encoding="utf-8") as file:
                        file.write(log_error_message)

                else:
                    print(log_error_message)

                raise

        return inner

    return wrapper
