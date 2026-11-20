# p3_exception.py 证明子线程的异常会被吞掉：在子线程里 raise ValueError，主线程 print("我还活着")，看会发生什么
import threading

def boom():
    raise ValueError("子线程炸了")

t = threading.Thread(target=boom)
t.start()
t.join()

print("主线程: 我还活着")