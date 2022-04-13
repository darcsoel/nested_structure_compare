from itertools import zip_longest


def check_if_list_contains_simple_data_types(list_):
    result = []

    for element in list_:
        if isinstance(element, (int, float, bool, str)):
            result.append(True)
        else:
            result.append(False)

    return all(result)


def get_simple_list_types_counter(list_):
    result = {"int": 0, "float": 0, "bool": 0, "str": 0}

    for element in list_:
        if isinstance(element, int):
            result["int"] += 1
        if isinstance(element, float):
            result["float"] += 1
        if isinstance(element, bool):
            result["bool"] += 1
        if isinstance(element, str):
            result["str"] += 1

    return result


def same_structure_as(original, other):
    result = []

    if isinstance(original, list) and isinstance(other, list):
        if check_if_list_contains_simple_data_types(original) and check_if_list_contains_simple_data_types(other):
            result.append(get_simple_list_types_counter(original) == get_simple_list_types_counter(other))
        else:
            for first, second in zip_longest(original, other):
                if type(first) == type(second):
                    if isinstance(first, list) and isinstance(second, list):
                        result.append(same_structure_as(first, second))
                    else:
                        result.append(True)
                else:
                    result.append(False)
    else:
        result.append(type(original) == type(other))

    return all(result)
