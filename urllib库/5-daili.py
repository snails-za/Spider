import urllib.request
import urllib.parse

url = r'http://www.baidu.com/baidu?wd=ip&tn=monline_7_dg&ie=utf-8'

# 创建handler
handler = urllib.request.ProxyHandler({"http": "120.83.111.83"})
# 创建opener
opener = urllib.request.build_opener(handler)

# 发送请求
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'

        }

request = urllib.request.Request(url=url, headers=headers)
response = opener.open(request)

with open("ip.html", "wb") as fp:
    fp.write(response.read())

