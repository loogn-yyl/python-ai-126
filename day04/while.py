# no.1
n = 3
while n > 0:
    print(n)
    n -= 1

print("发射")

# no.2
# 反复让用户输入，直到输入 q 为止
# 这里用列表模拟输入，真实程序里换成 input()
inputs = ["3", "7", "q"]
total = 0
i = 0

while True:
    s = inputs[i]
    i += 1
    if s == "q":
        break
    total += int(s)

print("累加结果:", total)