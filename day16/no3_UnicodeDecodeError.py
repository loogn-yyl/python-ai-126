text = "中文测试"
raw = text.encode("gbk")
print("原文      :", text)
print("GBK 字节  :", raw)
print("长度      :",len(text), "字符 /", len(raw), "字节")
print()
print("按 gbk 解回来:", raw.decode("gbk"))
print("按 utf-8 硬解:")
try:
    raw.decode("utf-8")
except UnicodeDecodeError as e:
    print("  ", e)
print()
bad = raw.decode("utf-8", errors="replace")
print("replace 后长度:", len(bad), "含替换符:", "\ufffd" in bad)
print("ignore  后长度:", len(raw.decode("utf-8", errors="ignore")))

bom = b"\xef\xbb\xbfabc"
print("原始字节  :", bom)
print("utf-8 解 :", repr(bom.decode("utf-8")), "长度", len(bom.decode("utf-8")))
print("utf-8-sig:", repr(bom.decode("utf-8-sig")), "长度", len(bom.decode("utf-8-sig")))
print()
print("比较      :", bom.decode("utf-8") == "abc", bom.decode("utf-8-sig") == "abc")