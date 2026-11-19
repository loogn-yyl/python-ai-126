# p2_no_await.py 证明 hello() 不执行：故意不 await，看看警告长什么样、程序退出码是多少
import asyncio

async def hello():
    return "hi"

print("还没执行  :", hello())
print("执行过了  :", asyncio.run(hello()))

hello()
print("没有 await, 看警告")