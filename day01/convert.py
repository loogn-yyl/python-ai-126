# convert.py 存储单位换算
gb = float(input("请输入 GB 数: "))

mb = gb * 1024
kb = mb * 1024

print(f"{gb} GB = {mb:.0f} MB")
print(f"{gb} GB = {kb:.0f} KB")
print(f"{gb} GB = {gb * 1024**3:.0f} 字节")
