import socket
host = socket.gethostname() 
print(host)
host = socket.gethostbyname("DESKTOP-7926951") # 获取自己的主机ip
print(host)
