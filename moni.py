
def know(a):#获取股票数据
    import requests

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

import socket

def send_msg(resp_dict):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #client.setblocking(False)
    ip = '127.0.0.1'
    '''t=Thread(target=con,args=(client,ip))
    t.start()
    t.join(timeout=5000)'''
    try:
        client.bind((ip,5700))
    except:
        pass

    client.connect((ip, 5700))
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
    #print("发送" + payload)
    
    client.send(payload.encode("utf-8"))
    client.close()
    return 0

import json

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




listdict ={}
n = start()

    #for monin in n :
for key ,value in n.items():
    moniname = key[:-3]
    #moninum = value
    all=know(moniname)
    moni = all[3]
    s = win(moni,value)
    ldk1 = listdict[key]
    ldk1.append(s)
    listdict[key] = ldk1
    if ldk1[-1] != ldk1[-2]:
        send_msg({'msg_type':'group','number':'759734002','msg':'[CQ:poke,qq={}]'.format('3184158662' + key + all)})
