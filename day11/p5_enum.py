# p5_enum.py 枚举：定义 OrderStatus 四个状态，验证 name / value / 按值反查 / 跟字符串比较的结果
from enum import Enum

class OrderStatus(Enum):
    PENDING = "pending"
    PAID = "paid"
    SHIPPED = "shipped"
    DONE = "done"

print(OrderStatus.PENDING)
print(OrderStatus.PENDING.name, OrderStatus.PENDING.value)
print(OrderStatus("paid"))
print(OrderStatus.PENDING == "pending")
print([s.value for s in OrderStatus])