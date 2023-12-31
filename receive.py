from func_timeout import func_set_timeout
import socket
import json

ListenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ListenSocket.bind(('127.0.0.1', 5800))
ListenSocket.listen(100)

HttpResponseHeader = '''HTTP/1.1 200 OK\r\n
Content-Type: text/html\r\n\r\n
'''


def request_to_json(msg):
    for i in range(len(msg)):
        # if msg['raw_message']!= None:
        # print(msg)
        if msg[i] == "{" and msg[-1] == "\n":
            return json.loads(msg[i:])
    return None

# 需要循环执行，返回值为json格式


@func_set_timeout(40)  # 设定函数执行时间
def rev_msg():  # json or None
    Client, Address = ListenSocket.accept()

    Request = Client.recv(1024).decode(encoding='utf-8')

    rev_json = request_to_json(Request)
    Client.sendall((HttpResponseHeader).encode(encoding='utf-8'))
    Client.close()
    return rev_json
