def type_check(*expected_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg, expected in zip(args, expected_types):
                if not isinstance(arg, expected):
                    raise TypeError(
                        f"аргумент {arg} должен быть типа {expected.name}, "
                        f"но получен {type(arg).name}"
                    )
            return func(*args, **kwargs)
        return wrapper
    return decorator
@type_check(int, int)
def add(a, b):
    return a + b
print(add(2, 3))
try:
    print(add(2, "3"))
except TypeError as e:
    print(f"ошибка: {e}")