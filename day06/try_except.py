# no.1
try:
    x = 10 / 0
except ZeroDivisionError:
    print("不能除以 0")

# no.2
def safe_int(s):
    try:
        return int(s)
    except ValueError:
        return None

print(safe_int("42"))
print(safe_int("abc"))

# no.3
try:
    n = int("10")
except ValueError:
    print("转换失败")
else:
    print("转换成功, 结果", n)
finally:
    print("无论如何都执行")

# no.4 什么错都接
# try:
    # do_something()
# except:     # except 后必须写具体的异常类型
    # pass

# no.5
# 写法一: 元组
try:
    value = int("abc")
except (ValueError, TypeError) as e:
    print("转换失败:", type(e).__name__)

# 写法二: 分开放, 处理方式不同
try:
    value = int("abc")
except ValueError:
    print("格式不对")
except TypeError:
    print("类型不对")

# no.6
def set_age(age):
    if age < 0:
        raise ValueError(f"年龄不能为负数: {age}")
    return age

try:
    set_age(-5)
except ValueError as e:
    print("被捕获:", e)

# no.7
class ScoreError(Exception):
    pass

def check(score):
    if score > 100:
        raise ScoreError("分数不能超过 100")
    return score

try:
    check(150)
except ScoreError as e:
    print("自定义异常:", e)