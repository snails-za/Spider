import requests
from selenium import webdriver

URL_list = list()

base_url = r'https://www.365yg.com/api/pc/feed/?min_behot_time=0&category=video_new&utm_source=toutiao&widen=1&tadrequire=true&as=A1955D1B344D2EE&cp=5DB46D82FECEFE1&_signature=KXfXpBAVdMuglu4-CnkOTil317'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}

r = requests.get(url=base_url, headers=headers)

# 先将json数据转化为dict格式的数据，然后取出数据信息
video_data = r.json()['data']
for video in video_data:
    # print(video)
    video_url = 'https://www.365yg.com' + video["source_url"]
    video_id = video["video_id"]
    group_id = video["group_id"]

    URL = {
        'video_id': video_id,
        'video_url': video_url,
        'group_id': group_id
    }
    URL_list.append(URL)
# for url in URL_list:
#     print(url)
json_url = r'https://vas.snssdk.com/video/openapi/v1/'

path = r'C:\Users\wangju\Desktop\Spider\chromedriver_win32\chromedriver.exe'
for vi_id in URL_list:

    getdata = {
        # 'aid': '1768',
        'action': 'GetPlayInfo',
        'video_id': vi_id["video_id"],
        'nobase64': 'false',
        'ptoken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NzIxMDQwMzksInZlciI6InYxIiwiYWsiOiJjZmMwNjdiYjM5ZmVmZjU5MmFmODIwODViNDJlNmRjMyIsInN1YiI6InBnY19ub3JtYWwifQ.Z8iJGhqrlTcCH0vCy34JhzcrVAxgOCZS1N5AcuMQK9M',
        'vfrom': 'xgplayer'
    }
    refer = 'https://www.ixigua.com/i' + vi_id['group_id']
    print(refer)
    get_headers = {
        'Host': 'vas.snssdk.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Authorization': 'HMAC-SHA1:2.0:1572252418355974084:cfc067bb39feff592af82085b42e6dc3:fcUkOEgN3LOTW8GP9Eed5/EABcg=',
        'Origin': 'https://www.ixigua.com',
        'Connection': 'keep-alive',
        'Referer': refer
    }

    r = requests.get(url=json_url, headers=get_headers, params=getdata)
    print(r.json())







