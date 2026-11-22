# 03 downloader

一句话：线程池批量下载，带限流和失败清单；实测串行 3.2 秒 → 并发 0.6 秒。

## 怎么跑
python downloader.py

## 用了什么
time / concurrent.futures.ThreadPoolExecutor / concurrent.futures.as_completed
## 遇到的问题

## 已知不足