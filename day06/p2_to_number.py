# p2_to_number.py 安全转数字：to_number(s)，能转成 int 就转 int，能转 float 就转 float，都不行返回 None

def to_number(s):
    try:
        return int(s)
    except ValueError:
        pass
    try:
        return float(s)
    except ValueError:
        return None

print(to_number("1"))
print(to_number("1.2"))
print(to_number("a"))