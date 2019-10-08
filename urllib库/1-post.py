import urllib.request
import urllib.parse

post_url = r'https://fanyi.baidu.com/sug'
word = input("请输入您需要查询的英文单词:")
form_data = {
        "kw": word
        }

# 发送请求的过程
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
        }
# 构建请求对象
request = urllib.request.Request(url=post_url, headers=headers)
form_data = urllib.parse.urlencode(form_data).encode()
# 发送请求
response = urllib.request.urlopen(request, data=form_data)

print(response.read().decode())





