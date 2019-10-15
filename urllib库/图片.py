import urllib.request
import urllib.parse
import re
import os

class SpiderImg(object):

    def __init__(self, url, get_url):
        """初始化"""
        self.url = url
        self.get_url = get_url

    def create_object(self, data, headers):
        """创建请求对象"""

        data = urllib.parse.urlencode(data)

        self.url += data

        return urllib.request.Request(url=self.url, headers=headers)

    def send_request(self, request):
        """发送请求并且打印结果"""
        response = urllib.request.urlopen(request)

        htmls = response.read().decode()
        img_links = re.findall(self.get_url, htmls)

        for img_link in img_links:
            print(img_link)
        return img_links

    def save_img(self, img_links):
        if not os.path.exists("image"):
            os.mkdir("image")
        if not os.path.exists("./image/%s/" % word):
            os.mkdir("./image/%s/" % word)
        count = 1

        for img_item in img_links:
            urllib.request.urlretrieve(url=img_item, filename=('./image/%s/%d.jpg' % (word, count)))
            count += 1


if __name__ == '__main__':
    url = r'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&'
    """
    pn : 第几张图片
    rn : 一张有多少个图片
    """
    word = input("请输入您想查询的图片名称（例如：美女，动物等）：")
    num = input("从第几张图片开始（一页60张）：")

    data = {'word': word,
            "pn": num,
            'rn': '60'}

    get_url = r'"thumbURL":.*?"(.*?\.jpg)"'

    headers = {
        'Host': 'image.baidu.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
        'Accept': 'text/plain, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
        'Referer': 'https://image.baidu.com/search/index?tn=baiduimage&st=-1&ipn=r&ct=201326592&nc=1&lm=-1&cl=2&ie=utf-8&word=%E5%8A%A8%E7%89%A9&ie=utf-8&istype=2&fm=se0',
        'Cookie': 'BDqhfp=%E5%8A%A8%E7%89%A9%26%26NaN-1undefined-1undefined%26%264630%26%267; BAIDUID=04AF0E6FCEB74A3E6CA2C32606EF8892:FG=1; BIDUPSID=D8CAC45F89186CC0232016FF853C7430; PSTM=1557136117; BDUSS=RISjJMQkdvREJSdWo0V2VvQlJ6MElVQmNHd3diWDFycE5zdXJ3NmNIT0E3MXhkSVFBQUFBJCQAAAAAAAAAAAEAAAC5XwWb17fRsDE2NTEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIBiNV2AYjVddH; indexPageSugList=%5B%22dongwu%22%2C%22meinv%22%2C%22%E5%8A%A8%E7%89%A9%22%2C%22%E9%A3%8E%E6%99%AF%22%2C%22%E6%96%97%E9%B1%BC%22%5D; H_PS_PSSID=1426_21082_29721_29567_29221_22159; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDRCVFR[Hp1ap0hMjsC]=mk3SLVN4HKm; delPer=0; PSINO=1; BCLID=12201827791489652894; BDSFRCVID=F5LOJeC627Sm8SnwCqGkuuATumJVeXcTH6aIS-WX22TRn74wT44REG0P_M8g0KubTVMxogKKy2OTH9DF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tJkOoK0afC83qPbv-P4_5bLSMMnXKK62aKDsKD51BhcqEIL4jpbVehtH5PbD0-ntbm6nLR6FQJ5iHUbSj4Qz0IuiWaKHLpjXJbnf-I-2Lq5nhMJ3Xj7JDMP0-ROpWRvy523iXCovQpPBshQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xXj_0-nDSHHKDtj8t3e; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; firstShowTip=1; userFrom=www.baidu.com; cleanHistoryStatus=0',

    }

    # 创建对象，初始化数据
    insect = SpiderImg(url, get_url)

    # 创建请求对象
    request = insect.create_object(data, headers)

    # 发送请求并且打印结果
    img_links = insect.send_request(request)

    # 保存图片
    insect.save_img(img_links)
    



