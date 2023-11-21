import psutil


pl = psutil.pids()
result = "PROCESS_IS_NOT_RUNNING"
print(psutil.Process(pl).name())
# for pid in pl:
#     print(psutil.Process(pid).name())
