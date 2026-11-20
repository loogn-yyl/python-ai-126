# no.4
import threading
import time

N = 2_000
counter_nolock = 0
lock = threading.Lock()
counter_lock = 0

def add_nolock():
    global counter_nolock
    for _ in range(N):
        v = counter_nolock
        time.sleep(0)     # 把 【读】 和 【写】 之间的窗口放大
        counter_nolock = v + 1

def add_lock():
    global counter_lock
    for _ in range(N):
        with lock:
            v = counter_lock
            time.sleep(0)
            counter_lock = v + 1

ts = [threading.Thread(target=add_nolock) for _ in range(4)]
for t in ts:
    t.start()
for t in ts:
    t.join()

ts = [threading.Thread(target=add_lock) for _ in range(4)]
for t in ts:
    t.start()
for t in ts:
    t.join() 

print("期望值:", 4 * N)
print("无锁结果正确:", counter_nolock == 4 * N)
print("有锁结果正确:", counter_lock == 4 * N)