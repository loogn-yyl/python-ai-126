# p2_make_multiplier.py 闭包工厂：make_multiplier(n) 返回「乘以 n」的函数，造 2 倍和 3 倍各一个
def make_multiplier(n):
    def multiply(x):
        return x * n

    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(10), triple(10))
print([double(i) for i in range(1, 4)])
print(double.__name__)