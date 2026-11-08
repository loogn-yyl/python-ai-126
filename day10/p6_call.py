# p6_call.py 像函数：Discount(0.8) 用 __call__ 打八折，验证 callable() 和列表推导式里能用
class Discount:
    def __init__(self, rate):
        self.rate = rate

    def __call__(self, price):
        return round(price * self.rate, 1)

vip = Discount(0.8)
print(vip(100), vip(59.0))
print(callable(vip), callable(0.8))
print([vip(p) for p in [200, 300, 50]])