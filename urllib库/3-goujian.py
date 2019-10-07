import urllib.request
import urllib.parse


url = r'http://www.baidu.com/'

# response = urllib.request.urlopen(url)

# print(response.read().decode())

# 自己要伪装的头部
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
        }

# 构建请求对象
request = urllib.request.Request(url=url, headers=headers)

# 发送请求
response = urllib.request.urlopen(request)
print(response.read().decode())

