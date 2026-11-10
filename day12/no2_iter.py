# no.2
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

cd = CountDown(2)
print(list(cd))
print("第二次 list 同一个对象:", list(cd))