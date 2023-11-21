import datetime
from chinese_calendar import is_workday
date = datetime.datetime.now().date()
if is_workday(date):
  print("是工作日")
else:
  print("是休息日")