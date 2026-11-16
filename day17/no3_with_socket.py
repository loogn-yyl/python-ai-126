# no.3
import socket

host, port = "example.com", 80
req = f"GET / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(10)
    s.connect((host, port))
    s.sendall(req.encode("ascii"))

    chunks = []
    while True:
        buf = s.recv(4096)
        if not buf:
            break
        chunks.append(buf)

raw = b"".join(chunks)
text = raw.decode("utf-8", errors="replace")
print("收到", len(raw), "字节")
print("首行:", text.split("\r\n")[0])