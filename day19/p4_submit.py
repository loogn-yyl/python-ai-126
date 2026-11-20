# p4_submit.py 用 submit 抓异常：同样的错误，用 f.result() 把它抛回主线程
from concurrent.futures import ThreadPoolExecutor

def boom():
    raise ValueError("子线程炸了")

with ThreadPoolExecutor(max_workers=1) as pool:
    f = pool.submit(boom)
    try:
        f.result()
    except ValueError as e:
        print("主线程抓到了:", type(e).__name__, e)