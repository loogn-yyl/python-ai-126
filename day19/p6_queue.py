# p6_queue.py 无锁计数器：复现第 5 节那个丢更新，然后用 queue.Queue 重写一版，不用锁也能对
import threading
import queue

N = 2_000
q = queue.Queue()
done = []

def work():
    subtotal = 0
    while True:
        item = q.get()
        if item is None:
            q.task_done()
            break
        subtotal += item
        q.task_done()
    done.append(subtotal)

threads = [threading.Thread(target=work) for _ in range(4)]
for t in threads:
    t.start()

for _ in range(N * 4):
    q.put(1)
for _ in range(4):
    q.put(None)

q.join()
for t in threads:
    t.join()

print("总计数:", sum(done))
print("正确:", sum(done) == N * 4)