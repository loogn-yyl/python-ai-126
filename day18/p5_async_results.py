# p5_async_results.py 带返回值的并发：gather 三个返回不同值的协程，验证结果顺序是传入顺序不是完成顺序
import asyncio

async def work(name, sec):
    print(f"  开始 {name}")
    await asyncio.sleep(sec)
    print(f"  结束 {name}")
    return name.upper()

async def main():
    results = await asyncio.gather(
        work("a", 0.3), work("b", 0.2), work("c", 0.1)
    )
    print("gather 结果:", results)

    done = []
    for w in asyncio.as_completed([work("a", 0.3), work("b", 0.2), 
                                   work("c", 0.1)]):
        done.append(await w)
    print("as_completed 结果:", done)

asyncio.run(main())