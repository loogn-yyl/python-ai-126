# p3_parse_response.py 拆响应报文：给一段原始响应文本，返回 (状态码, 头部字典, 正文)
def parse_response(raw):
    head, _, body = raw.partition("\r\n\r\n")
    lines = head.split("\r\n")
    status = int(lines[0].split()[1])
    headers = {}
    for line in lines[1:]:
        k, _, v = line.partition(": ")
        headers[k.lower()] = v
    return status, headers, body

raw = ("HTTP/1.1 404 Not Found\r\n"
       "Content-Type: text/plain\r\n"
       "\r\n"
       "not here")
status, headers, body = parse_response(raw)
print("状态码:", status)
print("头部  :", headers)
print("正文  :", body)