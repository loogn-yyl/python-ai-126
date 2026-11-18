# p2_build_request.py 拼请求报文：写一个 build_request(method, path, host, headers)，返回完整的 HTTP 请求字符串。注意末尾那个空行
def build_request(method, path, host, headers):
    lines = [f"{method} {path} HTTP/1.1", f"Host: {host}"]
    for k, v in (headers or {}).items():
        lines.append(f"{k}: {v}")
    lines.append("")
    lines.append("")
    return "\r\n".join(lines)

req = build_request("GET", "/index.html", "example.com",
                    {"User-Agent": "test/1.0", "Accept": "*/*"})
print(repr(req))
print()
print("以空行结尾:", req.endswith("\r\n\r\n"))