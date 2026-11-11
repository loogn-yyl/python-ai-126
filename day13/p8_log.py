# p8_log.py 日志装饰器（综合）：给通讯录的 add / delete 套上 @log，每次操作自动追加一行到 actions.log，再读出来打印
import functools
import os

LOG = "actions.log"

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(f"{func.__name__}({args[0]}) -> {result}\n")
        return result
    return wrapper

contacts = {}

@log
def add(name):
    contacts[name] = "13800001111"
    return "已添加"

@log
def delete(name):
    if name in contacts:
        del contacts[name]
        return "已删除"
    return "没找到"

if os.path.exists(LOG):
    os.remove(LOG)

print(add("张三"))
print(add("李四"))
print(delete("王五"))
print("剩余:", sorted(contacts))
print("--- 日志 ---")
print(open(LOG, encoding="utf-8").read().strip())

os.remove(LOG)