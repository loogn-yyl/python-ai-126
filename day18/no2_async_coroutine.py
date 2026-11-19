# no.2
import asyncio

async def hello():
    return "hi"

print("类型      :", type(hello).__name__)
print("是协程吗  :", asyncio.iscoroutine(hello))    # hello 是一个函数对象，不是协程对象
hello()    # 这样写是错的
print("程序跑完了")

c = hello()
print("类型      :", type(c).__name__)
print("是协程吗  :", asyncio.iscoroutine(c))
print("还没执行  :", "hello() 只是造了一个协程对象, 里面的代码一行都没跑")
c.close() 

r = asyncio.run(hello())
print("run 之后  :", r)