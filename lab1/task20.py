def unique_elements(lst):
    unique_set = set()
    def collect(element):
        if isinstance(element, list):
            for item in element:
                collect(item)
        else:
            unique_set.add(element)
    collect(lst)
    return list(unique_set)
list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2, 3]]]]
print(unique_elements(list_a))