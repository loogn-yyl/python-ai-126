# no.5
from pydantic import BaseModel, ValidationError

class Contact(BaseModel):
    name: str
    phone: str
    age: int = 0

c = Contact(name="张三", phone="13800001111", age="30")
print(c)
print(c.age, type(c.age).__name__)

try:
    Contact(name="李四", phone="139", age="abc")
except ValidationError as e:
    print("校验失败, 错误条数:", e.error_count())
    print("第一条:", e.errors()[0]["msg"])