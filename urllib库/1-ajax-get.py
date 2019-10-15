import urllib.request
import urllib.parse

url = r'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'


page = int(input("请输入想要的第几页数据:"))
# start=0 limit=20
number = 2

# 构建get参数
data = {
        'start': (page - 1) * number,
        "limit": number
        }

# 将字典转化为query_String
query_string = urllib.parse.urlencode(data)

# 
url += query_string

headers = {
        'Host': 'movie.douban.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Referer': 'https://movie.douban.com/typerank?type_name=%E6%8A%A8%E4%BD%9C&type=5&interval_id=100:90&action=',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
        'Cookie': 'bid=leg137Mdk98; douban-fav-remind=1; __utma=30149280.1017055945.1564279438.1570149063.1570680179.4; __utmz=30149280.1570149063.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; viewed="30336340"; ll="118371"; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1570680178%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_id.100001.4cf6=482cb2fb43308d27.1570149069.2.1570680501.1570149253.; __utma=223695111.945653536.1570149069.1570149069.1570680179.2; __utmz=223695111.1570149069.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __yadk_uid=wHJc7Y54OIW95ps6qAMSWzy1XvZSXwmp; _vwo_uuid_v2=D2C8DEAE7F683F212608C6EB0986075FC|bc90b42a8c7ab5770150858e066afc49; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utmb=30149280.0.10.1570680179; __utmc=30149280; __utmb=223695111.0.10.1570680179; __utmc=223695111'

        }

# 创建请求对象
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)
print(response.read().decode())
    


