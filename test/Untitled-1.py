#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

import time
from datetime import datetime
import pytz

tz = pytz.timezone('Asia/Shanghai') #东八区
#t = datetime.fromtimestamp(int(time.time()),pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S %Z%z')
t = datetime.fromtimestamp(int(time.time()),pytz.timezone('Asia/Shanghai')).strftime('%H:%M')


print(t)    # ==> 2017-12-05 18:39:45 CST+0800
#print(tz)
#tz=pytz.timezone('Asia/Shanghai').strftime('%Y-%m-%d %H:%M:%S %Z%z')
#print(tz)