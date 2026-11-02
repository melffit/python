def flatten_list(lst):
    flat_result = []
    def flatten(element):
        if isinstance(element, list):
            for item in element:
                flatten(item)
        else:
            flat_result.append(element)
    flatten(lst)
    lst.clear()
    lst.extend(flat_result)
list_a = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]
flatten_list(list_a)
print(list_a)