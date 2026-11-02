def cache(func):
    cache_dict = {}
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key in cache_dict:
            return cache_dict[key]
        result = func(*args, **kwargs)
        cache_dict[key] = result
        return result
    return wrapper
@cache
def multiply(a, b):
    print("вычисляю")
    return a * b
print(multiply(2, 3))
print(multiply(2, 3))
print(multiply(4, 5))