import urllib.request
import urllib.parse


url = r'http://www.baidu.com/baidu?'

word = input("请输入您想要搜索的内容：")

# 参数写成字典
data = {
        "wd": word,
        "tn": "monline_7",
        "ie": "utf-8",
        }

query_string = urllib.parse.urlencode(data)

url += query_string


# 发送请求
response = urllib.request.urlopen(url)

file_name = word + ".html"
with open(file_name, "wb") as fp:
    fp.write(response.read())


