# guessNum.py 猜数字：程序固定答案 42，最多让猜 3 次，猜中 break，用完次数提示失败

answer = 42
for i in range(3):
    x = int(input(f"第{i + 1}次猜数字: "))
    if x == answer:
        print("猜中了")
        break
    elif x < answer:
        print("小了")
    else:
        print("大了")
else:
    print(f"猜数字失败, 答案是{answer}")