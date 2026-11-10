# p2_CountDown.py 手写迭代器：CountDown(start) 用 __iter__ + __next__ 从 start 数到 1
class CountDown:
    def __init__(self, start):
        self.n = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        self.n -= 1
        return self.n + 1

for i in CountDown(3):
    print(i)

print(list(CountDown(5)))