# 03 downloader

一句话：线程池批量下载，5 个任务 3 个工作线程，实测 0.22 秒跑完。

## 怎么跑
python downloader.py

## 用了什么
time / concurrent.futures.ThreadPoolExecutor / concurrent.futures.as_completed

## 遇到的问题
- as_completed 谁先完成谁先返回，顺序不固定，所以进度只能按「已完成个数」计数，不能按任务序号
- submit 返回的是 future，要自己建一个 future → url 的字典，否则拿到结果不知道是哪个文件

## 已知不足
- download() 用 time.sleep 模拟，没有真网络请求；换成 requests 后必须加 timeout
- 没有失败清单：某个任务抛异常会让 f.result() 直接在循环里抛出，整个中断（要么 try/except 收集，要么用 futures 的 exception() 判断）