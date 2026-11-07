# p7_mro.py MRO：写 A / B(A) / C(A) / D(B, C)，打印 D.__mro__ 和 D().who()，解释为什么是 B

class A:
    def who(self):
        return "A"

class B(A):
    def who(self):
        return "B"

class C(A):
    def who(self):
        return "C"

class D(B, C):
    pass

print([k.__name__ for k in D.__mro__])
print(D().who())
print(D.__mro__)