import urllib.request

url = r'http://www.baidu.com'
# 完整的url  http://www.baidu.com:80/
# index.html?name=goudan&password=123#lala

response = urllib.request.urlopen(url)


print(response.geturl())
# print(response.read().decode())
# with open("baudu.html", "w") as fp:
    # fp.write(response.read().decode())
