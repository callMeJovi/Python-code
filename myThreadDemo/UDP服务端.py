from socket import *

# 最简化的UDP服务端代码
s = socket(AF_INET, SOCK_DGRAM)  # 创建UDP类型的套接字
# 绑定端口
s.bind(("127.0.0.1", 8888))  # 元组 (IP,端口) IP本机接受 端口要大于1024
print("waiting for receiving data")
recv_data = s.recvfrom(1024)  # 1024表示本次接收的最大字节数. 返回的recv_data是个元组
print(recv_data)
print(f"receive remote data {recv_data[0]}, from {recv_data[1]}")
s.close()
