# no.1
def make_counter():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner

c1 = make_counter()
print(c1(), c1(), c1())
c2 = make_counter()
print(c2())
print(c1())