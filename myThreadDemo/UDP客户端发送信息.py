from socket import *
# 最简化的UDP客户端发送消息代码
s = socket(AF_INET, SOCK_DGRAM)  # 建立联接 创建UDP类型的套接字
# define the address that we send the data to.
addr = ("127.0.0.1", 8888)
data = input("what's your input data")
s.sendto(data.encode("gbk"), addr)  # (send what, send to who)
s.close()
