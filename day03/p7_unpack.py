# p7 unpack.py 信息拆包：用列表存若干 (姓名, 年龄) 元组，遍历打印「张三 今年 18 岁」

students = [("张三", 18), ("李四", 28)]

for name, age in students:
    print(f"{name} 今年 {age} 岁")