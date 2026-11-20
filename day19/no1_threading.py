# no.1
import threading
import time

results = []

def fetch(i):
    time.sleep(0.05 * i)
    results.append(f"任务 {i} 完成")

threads = [threading.Thread(target=fetch, args=(i,)) for i in range(1, 4)]

for t in threads:
    t.start()
for t in threads:
    t.join()     # 等所有线程结束

print("结果:", results)
print("线程还活着吗:", any(t.is_alive() for t in threads))