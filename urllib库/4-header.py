import urllib.request
import urllib.parse

url = r'http://www.baidu.com'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
        }

# 创建一个handler
handler = urllib.request.HTTPHandler()
# 通过handler创建一个opener
# opener就是一个对象，一会发送请求的时候，直接使用里的方法即可，不要使用urlopen
opener = urllib.request.build_opener(handler)

# 发送请求
request = urllib.request.Request(url=url, headers=headers)

response = opener.open(request)

print(response.read().decode())


