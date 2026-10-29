# secondtotime.py 输入总秒数，换算成[时:分:秒]格式

total = int(input("请输入总秒数: "))

hour = total // (60 * 60)
minute = (total - hour * 60 * 60) // 60
second = total % (60 * 60) % 60

print(f"[{hour:02d}: {minute:02d}: {second:02d36}]")
