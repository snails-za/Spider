import requests


# 不带参数的get
"""
url = r"http://www.baidu.com"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}

r = requests.get(url, headers=headers)

# print(r.encoding)
r.encoding = "utf8"

print(r.text)
"""



# 带参数的get
url = r'https://www.baidu.com/baidu?tn=monline_3_dg&ie=utf-8'
data = {'wd': '中国'}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}

# parameters 参数
r = requests.get(url, headers=headers, params=data)

# with open("baudu.html", "wb") as fp:
#     fp.write(r.content)
print(r.status_code)
print(r.headers)
print(r.url)









