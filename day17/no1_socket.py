# no.1
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

print("family:", s.family, "-> AF_INET =", socket.AF_INET)
print("type:", s.type, "-> SOCK_STREAM =", socket.SOCK_STREAM)

s.close()
print("已关闭")