# no.1
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"

print(grade)

# no.2
for v in [0, 1, "", "a", [], [0], {}, None]:
    print(f"{repr(v):>8} -> {bool(v)}")

print(f"{'':>8} -> {bool('')}")
print(f"{' ':>8} -> {bool(' ')}")
print(f"{repr(''):>8} -> {bool('')}")
print(f"{repr(' '):>8} -> {bool(' ')}")

# no.3
a = [1, 2]
b = [1, 2]

print(a == b)   # 值一样吗
print(a is b)   # 是同一个对象吗

c = a
print(a is c)