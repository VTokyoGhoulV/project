def filter_by_state(dict_list: list, state: str = "EXECUTED") -> list:
    filtered_list = []

    for item in dict_list:
        if item["state"] == state:
            filtered_list.append(item)

    return filtered_list
