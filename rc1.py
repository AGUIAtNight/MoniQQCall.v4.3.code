from asyncio.windows_events import NULL
import requests


def know(a):#获取股票数据
    gudaima = a#"sz000001"
    headers = {'referer': 'http://finance.sina.com.cn'}
    resp = requests.get('http://hq.sinajs.cn/list=' + gudaima, headers=headers, timeout=6)
    data = resp.text
    return data 
    #print(data)
    '''
    var hq_str_sz000001="平安银行,17.450,17.330,17.350,17.560,17.210,17.350,17.360,148168295,2575115124.690,77830,17.350,69600,17.340,336500,17.330,321500,17.320,208200,17.310,370500,17.360,595600,17.370,497478,17.380,537000,17.390,815540,17.400,2022-01-21,15:00:03,00";

    输出内容含义，下面为各个数据的含义：

    0：”平安银行”，股票名字；
    1：”27.55″，今日开盘价；
    2：”27.25″，昨日收盘价；
    3：”26.91″，当前价格；
    4：”27.55″，今日最高价；
    5：”26.20″，今日最低价；
    6：”26.91″，竞买价，即“买一”报价；
    7：”26.92″，竞卖价，即“卖一”报价；
    8：”22114263″，成交的股票数，由于股票交易以一百股为基本单位，所以在使用时，通常把该值除以一百；
    9：”589824680″，成交金额，单位为“元”，为了一目了然，通常以“万元”为成交金额的单位，所以通常把该值除以一万；
    10：”4695″，“买一”申请4695股，即47手；
    11：”26.91″，“买一”报价；
    12：”57590″，“买二”
    13：”26.90″，“买二”
    14：”14700″，“买三”
    15：”26.89″，“买三”
    16：”14300″，“买四”
    17：”26.88″，“买四”
    18：”15100″，“买五”
    19：”26.87″，“买五”
    20：”3100″，“卖一”申报3100股，即31手；
    21：”26.92″，“卖一”报价
    (22, 23), (24, 25), (26,27), (28, 29)分别为“卖二”至“卖四的情况”
    30：”2008-01-11″，日期；
    31：”15:05:32″，时间；
    ————————————————
    版权声明：本文为CSDN博主「程序化交易」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
    原文链接：https://blog.csdn.net/meiaoxue1234/article/details/122648757
    '''

def mail():
        # smtplib 用于邮件的发信动作
    import smtplib
    # email 用于构建邮件内容
    from email.mime.text import MIMEText


    # 发信方的信息：发信邮箱，QQ 邮箱授权码
    from_addr = '3562230984@qq.com'
    password = 'kvzgvkntrfiqdafg'
    

    # 收信方邮箱
    to_addr = '981011972@qq.com'

    # 发信服务器
    smtp_server = 'smtp.qq.com'

    # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
    msg = MIMEText('my first email send by python','plain','utf-8')


    server = smtplib.SMTP_SSL(smtp_server)
    server.connect(smtp_server,465)

    server.login(from_addr, password)

    server.sendmail(from_addr, to_addr, msg.as_string())
    # 关闭服务器
    server.quit()


import socket
from threading import Thread
def con(ListenSocket,ip):
    ListenSocket.connect((ip, 5701))

def send_msg(resp_dict):
    #ListenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #ListenSocket.setblocking(False)
    ip = '127.0.0.1'
    t=Thread(target=con,args=(ListenSocket,ip))
    t.start()
    t.join(timeout=5)
    #con(ListenSocket,ip)
    msg_type = resp_dict['msg_type']  # 回复类型（群聊/私聊）
    number = resp_dict['number']  # 回复账号（群号/好友号）
    msg = resp_dict['msg']  # 要回复的消息
    # 将字符中的特殊字符进行url编码
    msg = msg.replace(" ", "%20")
    msg = msg.replace("\n", "%0a")
    if msg_type == 'group':
        payload = "GET /send_group_msg?group_id=" + str(
            number) + "&message=" + msg + " HTTP/1.1\r\nHost:" + ip + ":5700\r\nConnection: close\r\n\r\n"
    elif msg_type == 'private':
        payload = "GET /send_private_msg?user_id=" + str(
            number) + "&message=" + msg + " HTTP/1.1\r\nHost:" + ip + ":5700\r\nConnection: close\r\n\r\n"
    print("发送" + payload)
    ListenSocket.send(payload.encode("utf-8"))
    ListenSocket.close()
    return 0



def request_to_json(msg):
    for i in range(len(msg)):
        if msg[i]=="{" and msg[-1]=="\n":
            return json.loads(msg[i:])
    return None
#需要循环执行，返回值为json格式
def rev_msg():# json or None
    print('rev_msg')
    ListenSocket, Address = ListenSocket.accept()
    Request = ListenSocket.recv(1024).decode(encoding='utf-8')
    rev_json=request_to_json(Request)
    ListenSocket.sendall((HttpResponseHeader).encode(encoding='utf-8'))
    ListenSocket.close()
    print(rev_json)
    return rev_json


def rang(ziduan,n):
    for i in range(100):
        ziduan.setdefault(n + lenum3(i), 0)
        if ziduan[n + lenum3(i)] == 0:
            return i

def call ():
    print("rev")
    try:
        rev =rev_msg()
        print(rev)
    except:
        rev=None
        pass
    
    return rev

def lenum3(ln):
    if ln<100 and ln >10:#两位
        strln=str('0'+str(ln))
    if ln < 10 :
        strln=str('00'+str(ln))
    if ln > 100:
        strln=str(ln)
    return strln


def recall (ziduan):
    print (ziduan)
    import socket
    import requests
    import random
    rev=call()
    if rev != None:
        #print(rev["post_type"])
        if rev["post_type"] == "message":
            #print(rev) #需要功能自己DIY
            if rev["message_type"] == "private": #私聊
                if rev['raw_message']=='在吗':
                    qq = rev['sender']['user_id']
                    send_msg({'msg_type':'private','number':qq,'msg':'我在'})
            elif rev["message_type"] == "group": #群聊
                group = rev['group_id']
                if "[CQ:at,qq=3184158662]" in rev["raw_message"]:
                    if rev['raw_message'].split(' ')[1]=='设置':
                        qq=rev['sender']['user_id']
                        send_msg({'msg_type':'group','number':group,'msg':'[CQ:poke,qq={}]'.format(qq + '股票代码')})
                        rev=call()
                        if rev['raw_message'].split(' ')[1]!= None:
                            n= num(rev['raw_message'].split(' ')[1])
                            i = rang(ziduan,n)#rang
                            #ziduan[rev['raw_message'].split(' ')[1] + i] 
                            qq=rev['sender']['user_id']
                            send_msg({'msg_type':'group','number':group,'msg':'[CQ:poke,qq={}]'.format(qq + '价位')})
                            rev=call()
                            if rev['raw_message'].split(' ')[1]!= None:
                                ziduan[n + lenum3(i)]= str(rev['raw_message'].split(' ')[1])

                    '''if rev['raw_message'].split(' ')[1]=='帮助':
                        qq=rev['sender']['user_id']
                        send_msg({'msg_type':'group','number':group,'msg':'[CQ:poke,qq={}]'.format(qq) + ''})'''

            else:
                pass
        else:  # rev["post_type"]=="meta_event":
            pass

    return ziduan

def num(nu):
    if nu[0]=='6':
        nu == 'sh'+nu
    if nu[0] == '3' or nu[0]=='0':
        nu == 'sz'+nu
    return nu

def start():
    #listc = []


    try:
        with open('maintime.json','r')as TxtFile:
            maintime = json.load(TxtFile)
    except:
        maintime={}
        with open('maintime.json', 'w') as f:
            json.dump(maintime, f)

    return maintime


def win(now,value,key):
    now = float(now)
    value=float(value)
    if now < value :
        s=0
    if now == value :
        s=1 
    if now > value :
        s=2
    return s


def main (maintime):
    print(maintime)
    
    
    n=recall(maintime)
    #for monin in n :



import socket
import json

ListenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ListenSocket.setblocking(False)
ListenSocket.bind(('127.0.0.1', 5701))
ListenSocket.listen(100)
HttpResponseHeader = '''HTTP/1.1 200 OK
Content-Type: text/html
'''
maintime = start()
listdict ={}
while True:
    main(maintime)

    send_msg({'msg_type':'group','number':'759734002','msg':'[CQ:poke,qq={}]'.format('3184158662' )})
    print('1')
