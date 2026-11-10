# p1_iter_next.py 手动遍历：用 iter() / next() 遍历一个三元素列表，第四次进 except StopIteration 并打印「没有了」
nums = [10, 20, 30]
it = iter(nums)

while True:
    try:
        print(next(it))
    except StopIteration:
        print("没有了")
        break