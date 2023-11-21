import urllib.request

gudaima = "sz000001"
url = "http://qt.gtimg.cn/q=" + gudaima
response = urllib.request.urlopen(url)
result = response.read().decode('gbk')
print(result)
