# no.4
import requests

r = requests.get("https://example.com", timeout=10)

print("状态码:", r.status_code)
print("编码  :", r.encoding)
print("长度  :", len(r.text), "字符")
print("首60  :", r.text[:60].replace("\n", " "))