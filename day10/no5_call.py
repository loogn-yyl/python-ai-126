# no.5
class Multiplier:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return x * self.n

double = Multiplier(2)
triple = Multiplier(3)
print(double(5), triple(5))
print(callable(double), callable(5))
# callable 判断类型上有没有 __call__

books = ["C 程序设计", "流畅的 Python", "算法导论"]
print(list(map(double, [1, 2, 3])))
print(sorted(books, key=Multiplier(1)) == sorted(books))