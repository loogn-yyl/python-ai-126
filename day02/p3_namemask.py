# namemask.py 姓名脱敏：输入姓名「张三丰」，输出「张*丰」——保留首尾，中间用 * 

name =input("请输入姓名: ")

print(name[0] + "*" * (len(name) - 2) + name[-1])