def merge_dicts(dict_a, dict_b):
    for key, value_b in dict_b.items():
        if key not in dict_a:
            dict_a[key] = value_b
        else:
            value_a = dict_a[key]
            if isinstance(value_a, dict) and isinstance(value_b, dict):
                merge_dicts(value_a, value_b)
            elif isinstance(value_a, list) and isinstance(value_b, list):
                value_a.extend(value_b)
            elif isinstance(value_a, set) and isinstance(value_b, set):
                value_a.update(value_b)
            elif isinstance(value_a, tuple) and isinstance(value_b, tuple):
                dict_a[key] = value_a + value_b
            else:
                dict_a[key] = value_b
    return dict_a
dict_a = {"a": 1, "b": {"c": 1, "f": 4}}
dict_b = {"d": 1, "b": {"c": 2, "e": 3}}
merge_dicts(dict_a, dict_b)
print(dict_a)