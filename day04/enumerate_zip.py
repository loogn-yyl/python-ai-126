# no.1
fruits = ["苹果", "香蕉", "西瓜"]

for i, f in enumerate(fruits, start=1):    # start 默认从 0 开始
    print(f"{i}. {f}")

# no.2
names = ["张三", "李四"]
ages = [18, 20]

for n, a in zip(names, ages):
    print(n, a)