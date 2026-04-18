def filter_by_state(dict_list: list, state: str = "EXECUTED") -> list:
    """
    Принимает список словарей и возвращает отфильтрованный список по состоянию
    """
    filtered_list = []

    for item in dict_list:
        if item["state"] == state:
            filtered_list.append(item)

    return filtered_list


def sort_by_date(dict_list: list, is_reversed: bool = True) -> list:
    """
    Принимает список словарей и возвращает отсортированный список по дате
    """
    return sorted(dict_list, reverse=is_reversed, key=lambda x: (x.get("date") is None, x.get("date")))
