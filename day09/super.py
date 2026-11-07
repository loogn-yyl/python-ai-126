class A:
    def __init__(self):
        self.trace = ["A"]

class B(A):
    def __init__(self):
        super().__init__()
        self.trace.append("B")

class C(A):
    def __init__(self):
        A.__init__(self)
        self.trace.append("C")

class D(A):
    def __init__(self):
        self.trace = []

print("B:", B().trace)
print("C:", C().trace)
print("D:", D().trace)