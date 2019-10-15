import urllib.request
import urllib.parse


url = r'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'


city = input("请输入城市：")
page = int(input("青蒿素如第几页："))
size = int(input("请输入查询数量："))

form_data = {
        'cname': "",	
        'pid': "",	
        'keyword': city,
        'pageIndex': page,
        'pageSize': size
        }

headers = {
        'Host': 'www.kfc.com.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Length': '62',
        'Connection': 'keep-alive',
        'Referer': 'http://www.kfc.com.cn/kfccda/storelist/index.aspx',
        'Cookie': 'KLBRSID=a34b6eb1eda6f7a05724ede2e440cdc7|1570677169|1570676783; ASP.NET_SessionId=c5zvg42w3yar4nbty0cy335p; __utma=62931061.1386413001.1570730961.1570730961.1570730961.1; __utmb=62931061.1.10.1570730961; __utmc=62931061; __utmz=62931061.1570730961.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1'

        }


# 创建请求对象，惊醒伪装
request = urllib.request.Request(url=url, headers=headers)

# 发送请求
form_data = urllib.parse.urlencode(form_data).encode()
response = urllib.request.urlopen(url, form_data)



with open("kfc_city.txt", "w") as f:
    f.write(response.read().decode())










