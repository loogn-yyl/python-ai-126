# p6_chunked.py 分批：chunked(iterable, size) 把任意序列切成固定大小的块，注意最后一块不足也要交出去

def chunked(iterable, size):
    buf = []
    for x in iterable:
        buf.append(x)
        if len(buf) == size:
            yield buf
            buf = []

    if buf:
        yield buf

for c in chunked(range(7), 3):
    print(c)
print(list(chunked("abcdef", 2)))