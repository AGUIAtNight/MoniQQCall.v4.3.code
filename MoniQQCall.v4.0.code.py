
import time
import shutil
import os
import socket
import json
import logging
# from re import T


# 默认的warning级别，只输出warning以上的
# 使用basicConfig()来指定日志级别和相关信息

logging.basicConfig(level=logging.DEBUG  # 设置日志输出格式
                    , filename="demo.log"  # log日志输出的文件位置和文件名
                    , filemode="w"  # 文件的写入格式，w为重新写入文件，默认是追加
                    # 日志输出的格式
                    # -8表示占位符，让输出左对齐，输出长度都为8位
                    # 时间输出的格式
                    , format="%(asctime)s - %(name)s - %(levelname)-9s - %(filename)-8s : %(lineno)s line - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
                    )

'''logging.debug("This is  DEBUG !!")
logging.info("This is  INFO !!")
logging.warning("This is  WARNING !!")
logging.error("This is  ERROR !!")
logging.critical("This is  CRITICAL !!")
'''
# 在实际项目中，捕获异常的时候，如果使用logging.error(e)，只提示指定的logging信息，不会出现
# 为什么会错的信息，所以要使用logging.exception(e)去记录。


# from asyncio.windows_events import NULL
# from ast import Str
# from asyncio.windows_events import NULL
# from threading import Thread


# event = threading.Event()


def send_msg(resp_dict):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client.setblocking(False)
    ip = '127.0.0.1'
    '''t=Thread(target=con,args=(client,ip))
    t.start()
    t.join(timeout=5000)'''
    '''try:
        client.bind((ip,5700))
    except:
        pass'''

    client.connect((ip, 5700))
    # print('com')
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
    # print("发送" + payload)

    client.send(payload.encode("utf-8"))
    client.close()
    return 0


def rang(ziduan, n):
    for i in range(100):
        ziduan.setdefault(n + lenum3(i), 0)
        with open('maintime.json', 'w') as f:
            json.dump(ziduan, f)
        if ziduan[n + lenum3(i)] == 0:
            return str(n + lenum3(i))


def call():
    from receive import rev_msg
    # print("rev")

    '''t=Thread(target=rev_msg)
    t.start()
    t.join(3)'''

    rev = rev_msg()

    # print(rev)
    return rev


def lenum3(ln):
    if ln < 100 and ln > 10:  # 两位
        strln = str('0'+str(ln))
    if ln < 10:
        strln = str('00'+str(ln))
    if ln > 100:
        strln = str(ln)
    return strln


def recall(ziduan):
    # print (ziduan)
    import socket
    import requests
    import random
    rev = call()
    if rev != None:
        # print(rev["post_type"])
        if rev["post_type"] == "message":
            # print(rev) #需要功能自己DIY
            if rev["message_type"] == "private":  # 私聊
                if rev['raw_message'] == '在吗':
                    qq = rev['sender']['user_id']
                    send_msg({'msg_type': 'private', 'number': qq, 'msg': '我在'})
            elif rev["message_type"] == "group" and rev['group_id'] == 759734002:  # 群聊
                group = '759734002'  # rev['group_id']
                # if "[CQ:at,qq=3184158662]" in rev["raw_message"]:
                if rev['raw_message'] == '设置':
                    qq = rev['sender']['user_id']
                    send_msg({'msg_type': 'group', 'number': group,
                             'msg': '输入股票代码（设置股票策略）'})

                    send_msg({'msg_type': 'group', 'number': group,
                             'msg': '输入‘已有’（查看已有策略或删除策略）'})

                if len(rev['raw_message']) == 6 and rev['raw_message'].isdigit() == True:
                    n = num(rev['raw_message'])
                    global i
                    i = rang(ziduan, n)  # rang
                    saver(ziduan)
                    qq = rev['sender']['user_id']
                    send_msg(
                        {'msg_type': 'group', 'number': group, 'msg': '监控价位,需要小数点'})
                    send_msg(
                        {'msg_type': 'group', 'number': group, 'msg': '现价,则输入“现价”'})
                    send_msg({'msg_type': 'group', 'number': group,
                             'msg': '监控新高低,则输入“监控”'})
                    # if rev['raw_message'].split(' ')[1]!= None:

                    # ziduan[rev['raw_message'].split(' ')[1] + i]

                if rev['raw_message'] == '现价' or ('.' in rev['raw_message']) == True or rev['raw_message'] == '监控':

                    ziduan[i] = str(rev['raw_message'])
                    saver(ziduan)
                    send_msg(
                        {'msg_type': 'group', 'number': group, 'msg': '设置成功'})
                    '''if rev['raw_message'].split(' ')[1]=='帮助':
                        qq=rev['sender']['user_id']
                        send_msg({'msg_type':'group','number':group,'msg':'[CQ:poke,qq={}]'.format(qq) + ''})'''
                if rev['raw_message'] == '已有':
                    for key, value in ziduan.items():
                        value = str(value)
                        send_msg({'msg_type': 'group', 'number': group,
                                 'msg': '{}'.format(key+','+value)})
                    send_msg({'msg_type': 'group', 'number': group,
                             'msg': '输入删除以上代码即可删除，如"删除sh600059002"'})
                    # print('输入删除+以上代码即可删除，如"删除+sh600059002"')
                if ('删除' in rev['raw_message']) == True:
                    sc = rev['raw_message'][2:]
                    removed_value = ziduan.pop(sc, '没有该策略')
                    saver(ziduan)

                    if removed_value != '没有该策略':
                        removed_value = '已删除该策略'

                    send_msg(
                        {'msg_type': 'group', 'number': group, 'msg': removed_value})

            else:
                pass
        else:  # rev["post_type"]=="meta_event":
            pass

    return ziduan


def num(nu):
    # print(nu[0])
    if nu[0] == '6':
        nu = 'sh'+nu
    if nu[0] == '3' or nu[0] == '0':
        nu = 'sz'+nu
    return nu


def test3():

    return1 = os.system('ping 180.76.76.76')

    if return1:

        lianjie = 1

    else:

        lianjie = 0  # '有网络'

    return lianjie


def start():
    while test3() != 0:
        time.sleep(3)
    import datetime
    from chinese_calendar import is_workday
    date = datetime.datetime.now().date()
    try:
        if is_workday(date):
            workday = 1
        else:
            workday = 0
    except Exception as e:
        workday = 1
        logging.exception(e)

    # if test3() == 0:
        # listc = []
    import os

    os.system("go-cqhttp.bat")

    setDir('datag')

    try:
        with open('maintime.json', 'r')as TxtFile:
            maintime = json.load(TxtFile)
    except Exception as e:
        maintime = {}
        with open('maintime.json', 'w') as f:
            json.dump(maintime, f)
        logging.exception(e)

    '''try:
        with open('mainsave.json', 'r')as TxtFile:
            mainsave = json.load(TxtFile)
    except:
        mainsave = {}
        with open('mainsave.json', 'w') as f:
            json.dump(mainsave, f)'''
    # else:
    #     start()
    return maintime, workday


def gtimgknow(a):
    import requests

    gudaima = a  # "sz000001"
    # headers = {'referer': 'http://finance.sina.com.cn'}
    resp = requests.get('http://qt.gtimg.cn/q=' + gudaima, timeout=6)
    a1 = resp.text
    data = a1.split('=')[1].split('~')
    return data
    '''
    view plain copy
    v_sz000858="51~五 粮 液~000858~176.98~177.91~177.05~85386~41383~44004~176.98~197~176.97~495~176.96~12~176.95~67~176.94~18~176.99~38~177.00~481~177.01~8~177.02~17~177.03~4~~20220809161448~-0.93~-0.52~178.00~176.22~176.98/85386/1511033063~85386~151103~0.22~27.62~~178.00~176.22~1.00~6869.47~6869.67~7.00~195.70~160.12~0.59~241~176.96~15.87~29.39~~~1.21~151103.3063~0.0000~0~ ~GP-A~-19.42~0.75~1.71~22.64~18.94~254.19~146.09~-7.34~-6.85~16.31~3881497761~3881608005~18.03~-11.87~3881497761~~~-22.03~-0.01~"; ;
    以 ~ 分割字符串中内容，下标从0开始，依次为
    view plain copy
    0: 未知
    1: 名字
    2: 代码
    3: 当前价格
    4: 昨收
    5: 今开
    6: 成交量（手）
    7: 外盘
    8: 内盘
    9: 买一
    10: 买一量（手）
    11-18: 买二 买五
    19: 卖一
    20: 卖一量
    21-28: 卖二 卖五
    29: 最近逐笔成交
    30: 时间
    31: 涨跌
    32: 涨跌%
    33: 最高
    34: 最低
    35: 价格/成交量（手）/成交额
    36: 成交量（手）
    37: 成交额（万）
    38: 换手率
    39: 市盈率
    40:
    41: 最高
    42: 最低
    43: 振幅
    44: 流通市值
    45: 总市值
    46: 市净率
    47: 涨停价
    48: 跌停价'''


def know(a):  # 获取股票数据
    import requests

    gudaima = a  # "sz000001"
    headers = {'referer': 'http://finance.sina.com.cn'}
    resp = requests.get('http://hq.sinajs.cn/list=' +
                        gudaima, headers=headers, timeout=6)
    data = resp.text
    return data
    # print(data)
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


def setDir(filepath):
    '''
    如果文件夹不存在就创建，如果文件存在就清空！
    :param filepath:需要创建的文件夹路径
    :return:
    '''
    if not os.path.exists(filepath):
        os.mkdir(filepath)
    else:
        shutil.rmtree(filepath)
        os.mkdir(filepath)


def win(now, value):
    if now != ' ':
        now = float(now)
        value = float(value)
        if now < value:
            s = 0
        if now == value:
            s = 1
        if now > value:
            s = 2
    else:
        s = None
    return s


def timenow():
    global tsw
    import time
    from datetime import datetime
    import pytz
    t = datetime.fromtimestamp(int(time.time()), pytz.timezone(
        'Asia/Shanghai')).strftime('%H:%M')
    tz = t.split(':')
    ta = tb = tc = td = te = tf = 0
    if int(tz[0]) >= 9:
        ta = 1
    if int(tz[0]) < 11:
        tb = 1
    if int(tz[0]) < 15:
        tc = 1
    if int(tz[0]) >= 13:
        td = 1
    if int(tz[0]) == 9 and int(tz[1]) > 30:
        te = 1
    if int(tz[0]) == 11 and int(tz[1]) < 30:
        tf = 1
    if ta == tb == 1 or tc == td == 1 or ta == tf == 1 or te == tb == 1:
        times = True
    else:
        times = False
    if t == '9:30' and tsw == False:
        send_msg({'msg_type': 'group', 'number': '759734002', 'msg': '早盘开始'})
        tsw = True

    if t == '11:30' and tsw == False:
        send_msg({'msg_type': 'group', 'number': '759734002', 'msg': '早盘结束'})
        tsw = True
    if t == '13:00' and tsw == False:
        send_msg({'msg_type': 'group', 'number': '759734002', 'msg': '午盘开始'})
        tsw = True
    if t == '15:00' and tsw == False:
        send_msg({'msg_type': 'group', 'number': '759734002', 'msg': '午盘结束'})
        tsw = True
    return times


def saver(n):

    with open('maintime.json', 'w') as f:
        json.dump(n, f)


def main(maintime, mainsave):
    # print(maintime)

    time.sleep(1)
    n = recall(maintime)
    t1 = timenow()

    if t1 == True:
        # logging.info(str(t1))
        logging.info('timenow')

        # time.sleep(1)
        for key, value in n.items():

            moniname = key[:-3]
            # moninum = value
            all = know(moniname).split('=')[1].split(',')
            # print(all)
            moni = all[3]
            name = all[0]
            openmoni = all[1]
            time.sleep(0.1)

            try:
                # if len(monilist) < 2:
                monilist = mainsave[name]

                monilist.append(moni)
                # else:

            except Exception as e:
                monilist = []
                logging.exception(e)

            if len(monilist) > 1:
                monixie = (
                    (float(monilist[-1])-float(monilist[0]))/float(openmoni))*100
                logging.info(name+str(monixie))
                # print(monixie)
                if monixie > 1 or monixie < -1:
                    send_msg({'msg_type': 'group', 'number': '759734002',
                              'msg': '{}异动'.format(str(name))+',价格{}'.format(str(moni))+',斜率{}'.format(str(monixie))})
            if len(monilist) != 0:
                monilist = [monilist[-1]]

            mainsave[name] = monilist

            if value == '现价':
                # time.sleep(0.5)
                global valuen
                valuen += 1
                send_msg({'msg_type': 'group', 'number': '759734002',
                         'msg': '现价{}'.format(name + ' ' + moni)})
                if valuen == 5:
                    valuen = 0
                    n[value] = 0
                    saver(n)

            if value == '监控':
                # global topdown
                '''
                3：”26.91″，当前价格；
                47: 涨停价
                48: 跌停价'''

                topdown1 = False
                topdown = False
                for i in range(3):
                    time.sleep(0.5)
                    gtimg1 = gtimgknow(moniname)
                    moni = gtimg1[3]
                    if moni == gtimg1[47] or moni == gtimg1[48]:
                        topdown = True
                    else:
                        topdown == False

                    if topdown1 == True and topdown == False:
                        send_msg(
                            {'msg_type': 'group', 'number': '759734002', 'msg': '{}开板'.format(name)})

                    if topdown == True and topdown1 == False:
                        send_msg(
                            {'msg_type': 'group', 'number': '759734002', 'msg': '{}封板'.format(name)})

                    topdown1 = topdown

            else:
                try:
                    with open('datag\\{}'.format(key)+'.json', 'r') as f:
                        ldk1 = json.load(f)
                except Exception as e:
                    ldk1 = []
                    with open('datag\\{}'.format(key)+'.json', 'w') as f:
                        json.dump(ldk1, f)
                    logging.exception(e)

                s = win(moni, value)
                # ldk1 = listdict[key]
                ldk1.append(s)
                with open('datag\\{}'.format(key)+'.json', 'w') as f:
                    json.dump(ldk1, f)
                # listdict[key] = ldk1
                try:
                    if ldk1[-1] != ldk1[-2]:
                        send_msg({'msg_type': 'group', 'number': '759734002',
                                 'msg': '{}'.format(name + ' ' + moni)})
                except Exception as e:
                    logging.exception(e)
                    pass
    else:
        time.sleep(1)

    # listdict ={}


# 引入psutil模块

# 判断某个程序是否在运行
# 原理：获取正在运行程序的pid，通过pid获取程序名，再按程序名进行判断

# def ifProcessRunning(process_name):
#     pl = psutil.pids()
#     result = False
#     for pid in pl:
#         if (psutil.Process(pid).name() == process_name):
#             if isinstance(pid, int):
#                 result = True
#     return result


# Python判断程序是否运行
# https://blog.csdn.net/capsclock/article/details/128374581
tsw = False
maintime,  workday = start()
valuen = 0
# python如何获取字典的key与value
# https://www.yisu.com/zixun/486098.html#:~:text=keys%20%E5%87%BD%E6%95%B0%E7%9A%84%E5%8A%9F%E8%83%BD%EF%BC%9A%E8%8E%B7%E5%8F%96%E5%BD%93%E5%89%8D%E5%AD%97%E5%85%B8%E7%9A%84%E6%89%80%E6%9C%89%E9%94%AE%20%28key%29%20keys,%E5%87%BD%E6%95%B0%E7%9A%84%E7%94%A8%E6%B3%95%EF%BC%9Adict.keys%20%28%29%20%EF%BC%8C%E6%97%A0%E9%9C%80%E4%BC%A0%E5%8F%82%EF%BC%8C%E8%BF%94%E5%9B%9E%E4%B8%80%E4%B8%AA%20key%20%E9%9B%86%E5%90%88%E7%9A%84%E4%BC%AA%E5%88%97%E8%A1%A8
# maintimekeys = maintime.keys()
mainsave = {}

i = 0
i1 = 0
while True:
    time.sleep(0.01)
    # rev = call()
    # if workday == 1:
    try:

        i1 += 1
        # print(i)
        # logging.info("This is  INFO !!")
        if i1 == 30:
            # run = ifProcessRunning('go-cqhttp.exe')
            # if run == False:
            #     logging.info('由于go-cqhttp.exe关闭而退出')
            #     break
            tsw = False
            i1 = 2
        main(maintime, mainsave)
        if i1 == 1:
            send_msg({'msg_type': 'group', 'number': '759734002',
                      'msg': '{}'.format('系统启动成功')})

        # send_msg({'msg_type':'group','number':'759734002','msg':'1'})
        # print('1')

    except Exception as e:
        # logging.error(e)

        if i1 > 20:
            i1 = 0

        logging.exception(e)
        continue
