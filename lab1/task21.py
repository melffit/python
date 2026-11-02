import time
def timing(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed_ms = (end - start) * 1000
        print(f"функция {func.name} выполнилась за {elapsed_ms:.2f} мс")
        return result
    return wrapper
@timing
def slow_function():
    time.sleep(1)
    return "готово"
print(slow_function())