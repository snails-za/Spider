import urllib.request

# url = r'http://www.baidu.com'
# 完整的url  http://www.baidu.com:80/
# index.html?name=goudan&password=123#lala

# response = urllib.request.urlopen(url)

# print(response.geturl())
# print(dict(response.getheaders()))
# print(response.read())
# print(response.read().decode())
# with open("baudu.html", "w") as fp:
    # fp.write(response.read().decode())
# print(response.getcode())
# print(response.readlines())
#with open("baidu.html", "wb") as f:
   # f.write(response.read())


# 下载图片
img_url = r'http://pics.sc.chinaz.com/files/pic/pic9/201901/zzpic16198.jpg'
# response = urllib.request.urlopen(img_url)

# with open("img1.jpg", "wb") as f:
   # f.write(response.read())
urllib.request.urlretrieve(img_url, "img3.jpg")


