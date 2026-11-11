# no.2
def my_decorator(func):
    def wrapper():
        print("  调用前")
        func()
        print("  调用后")

    return wrapper

def hello():
    print("你好")

hello2 = my_decorator(hello)
hello2()
print("---")
my_decorator(hello)()

@my_decorator
def hi():
    print("hi")

print("---")
hi()
# help(hi)