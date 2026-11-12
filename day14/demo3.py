from contacts import Contact

cases = [("   ", "13800001111"), ("张三", "138"), ("张三", "1380000111a")]

for args in cases:
    try:
        Contact(*args)
    except ValueError as e:
        print("拒绝:", e)