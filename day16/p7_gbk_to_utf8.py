# p7_gbk_to_utf8.py GBK 转 UTF-8：一段 GBK 字节，转成 UTF-8 字节，再各自解回字符串验证
gbk_bytes = "用户名,数量".encode("gbk")
utf8_bytes = gbk_bytes.decode("gbk").encode("utf-8")

print("GBK  :", gbk_bytes, len(gbk_bytes), "字节")
print("utf-8:", utf8_bytes, len(utf8_bytes), "字节")
print("解回来:", utf8_bytes.decode("utf-8"))
print("一致吗:", utf8_bytes.decode("utf-8") == gbk_bytes.decode("gbk"))