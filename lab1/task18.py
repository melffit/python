import datetime
def log_calls(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(filename, "a", encoding="utf-8") as f:
                f.write(f"{time} | {func.name} | args={args}, kwargs={kwargs}\n")
            return func(*args, **kwargs)
        return wrapper
    return decorator
@log_calls("log.txt")
def add(a, b):
    return a + b
add(2, 3)
add(10, 20)