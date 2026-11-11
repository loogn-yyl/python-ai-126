# no.8
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("actions.log", "a", encoding="utf-8") as f:
            f.write(f"{func.__name__}({args[0]}) -> {result}\n")
        return result
    return wrapper