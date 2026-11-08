# no.2-1
class A:
    def __init__(self, v):
        self.v = v

class B:
    def __init__(self, v):
        self.v = v

    def __eq__(self, other):
        if not isinstance(other, B):
            return NotImplemented
        return self.v == other.v

print("没写 __eq__:", A(1) == A(1))
print("写了 __eq__:", B(1) == B(1))
print("值不同:", B(1) == B(2))
print("跟别的类型比:", B(1) == 1)

# no.2-2
class A:
    def __init__(self, v):
        self.v = v

    def __eq__(self, other):
        return isinstance(other, A) and self.v == other.v

class B:
    def __init__(self, v):
        self.v = v

    def __eq__(self, other):
        return isinstance(other, B) and self.v == other.v

    def __hash__(self):
        return hash(self.v)

print("能比较:", A(1) == A(1))
try:
    print(set([A(1)]))
except TypeError as e:
    print("TypeError:", e)

print("能比较:", B(1) == B(1))
try:
    print(set([B(1)]))
except TypeError as e:
    print("TypeError:", e)