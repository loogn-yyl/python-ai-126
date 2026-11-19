# D018 笔记 · 异步编程

## 一句话
异步解决的是「等」——IO 密集才有用，CPU 密集一点快不了。  
烧水可以同时烧三壶（IO），切菜只有两只手（CPU）。

## IO 密集 vs CPU 密集
- IO 密集：等网络/磁盘/数据库，CPU 闲着   → asyncio / 线程池
- CPU 密集：循环/加密/图像处理，CPU 满载  → 多进程（GIL 挡住多线程）

## GIL
同一时刻只有一个线程执行 Python 字节码  
→ 多线程做计算不会变快  
→ 但线程等 IO 时会释放 GIL → 这是线程池能加速 IO 的原因
→ asyncio 不吃这一套：只有一条线程，靠 await 主动让出

## 协程
- async def f()   = 声明（允许里面出现 await）
- f()             = 造了一个协程对象，一行都没跑 ★和生成器一样是惰性的
- await x         = 暂停在这里，把 CPU 让给别人
- asyncio.run(main()) = 启动事件循环，跑完就关（一个程序只调一次）

## 三件套
async def / await / asyncio.gather  
★ 光加 async/await 不会变快，顺序 await 还是 0.6 秒  
gather(*coros) → 一起发出去，耗时 = 最慢那个  
★ gather 结果按「传入顺序」，不是完成顺序  
as_completed → 按完成顺序（拿结果时不能再按下标对应输入）

## 事件循环
- 单线程调度：就绪队列 → 跑 → 遇 await 挂起 → 查等待队列 → 挪回
- 所有协程同一个线程 → 切换成本极低但不为零，且也没有数据竞争  
  但 → 任何一处阻塞，整个程序停

## 两个坑
- time.sleep(s)     阻塞整个线程，事件循环停摆 → await asyncio.sleep(s)  
  症状：用了 gather 还是 0.6 秒，输出变成「开始-结束-开始-结束」，不报错
- requests 是同步的 一样会卡 → aiohttp / httpx，或 loop.run_in_executor  
  run_in_executor(None, f, a, b)  参数平铺，返回值要 await  
  默认线程池 min(32, cpu+4)，并发度被它卡住

## Semaphore 限流
asyncio.Semaphore(3) → 同时最多 3 个   
抓 1000 个页面一次全发出去 = 打人家服务器 + 自己连接耗尽  
限流不是优化，是必需品

## 超时
await asyncio.wait_for(coro, timeout=0.5) → TimeoutError

## 纪律
- 快了必须验证结果一样：assert sync_results == async_results
- 并发程序的错不是慢，是「快了但结果悄悄变了」
- 计时只记量级，:.2f 会抖动，别当 bug

## 踩过的坑
as_completed 只承诺完成顺序, 不保证启动顺序, 而且不同机器启动顺序也不同  
原因: 执行时把协程组塞进一个集合, 集合的顺序由元素的哈希值决定而且不同机器结果不同   
改进: 用 asyncio.create_task