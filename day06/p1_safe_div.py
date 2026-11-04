# p1_safe_div.py 安全除法：safe_div(a, b)，除数为 0 时返回 None 而不是崩

def safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

print(safe_div(1, 2))
print(safe_div(1, 0))