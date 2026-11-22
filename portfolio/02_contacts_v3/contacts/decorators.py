"""跟通讯录业务无关的小工具, 只依赖 functools。"""
import functools

LOG = "actions.log"

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        try:
            with open(LOG, "a", encoding="utf-8") as f:
                f.write(f"{func.__name__}: {result}\n")
        except OSError:
            pass
        return result
    return wrapper