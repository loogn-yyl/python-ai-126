# p1_threading.py threading 基线：三个线程各 sleep(0.1)，用 start() + join() 两轮循环，验证总耗时约 0.1 秒
import threading
import time

DELAY = 0.1

t0 = time.perf_counter()
ts = [threading.Thread(target=time.sleep, args=(DELAY,)) for _ in range(3)]
for t in ts:
    t.start()
for t in ts:
    t.join()
print(f"threading: {time.perf_counter() - t0:.1f} 秒")