# p2_leap.py 判断闰年：输入年份，能被 4 整除且不能被 100 整除，或能被 400 整除 → 闰年
years = int(input("请输入年份: "))

if years % 4 == 0 and years % 100 is not 0 or years % 400 == 0:
    print("是闰年")
else:
    print("不是闰年")