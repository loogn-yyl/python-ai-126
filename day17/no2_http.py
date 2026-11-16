# no.2
host = "example.com"

request = (
    f"GET / HTTP/1.1\r\n"
    f"Host: {host}\r\n"
    f"Connection: close\r\n"
    f"\r\n"
)

print("报文长度:", len(request), "字节")
print("逐行拆开 (repr 让 \\r\\n 显形):")
for line in request.split("\r\n"):
    print("   ", repr(line))

raw = (
    "HTTP/1.1 200 OK\r\n"
    "Content-Type: text/html; charset=utf-8\r\n"
    "Content-Length: 61\r\n"
    "\r\n"
    "<html><head><title>示例站点</title></head><body>hi</body></html>"
)

head, _, body = raw.partition("\r\n\r\n")
lines = head.split("\r\n")

print("状态行:", lines[0])
print("版本  :", lines[0].split()[0])
print("状态码:", lines[0].split()[1])
print()
headers = {}
for line in lines[1:]:
    k, _, v = line.partition(": ")
    headers[k] = v
print("头部  :", headers)
print("编码  :", headers["Content-Type"].split("charset=")[1])
print()
print("正文  :", body)