import requests
from bs4 import BeautifulSoup


class SpiderSys(object):
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers
        self.s = requests.Session()

    def dowmload_img(self):
        sub_img = self.s.get(self.url, headers=self.headers)
        # print(r.text)
        soup = BeautifulSoup(sub_img.text, 'lxml')
        # sub_img = re.findall(r'src="(.*?)"', str(soup.select("img[id='imgCode']")[0]))[0]
        sub_img = soup.select('img[id="imgCode"]')[0]['src']
        # print(sub_img)
        img_url = "https://so.gushiwen.org" + sub_img
        # print(type(img_url))
        # 通过会话获取图片链接
        img_n = self.s.get(url=img_url, headers=self.headers)
        # img_n.encoding = 'UTF8'
        # print(img_n.text)
        # urllib.request.urlretrieve(img_n.text, "imgCode.png")
        with open("imgCode.png", "wb") as f:
            f.write(img_n.content)
        # 获取类似cookie之类的验证信息参数
        self.__VIEWSTATE = soup.find("input", id="__VIEWSTATE")['value']
        self.__VIEWSTATEGENERATOR = soup.find("input", id="__VIEWSTATEGENERATOR")['value']
        # print(self.__VIEWSTATE)
        # print(self.__VIEWSTATEGENERATOR)

    def login(self):
        url = r'https://so.gushiwen.org/user/login.aspx?from=http%3a%2f%2fso.gushiwen.org%2fuser%2fcollect.aspx'
        # 提示用户输入验证码
        code = input("请输入验证码：")
        formdata = {
            '__VIEWSTATE': self.__VIEWSTATE,
            '__VIEWSTATEGENERATOR': self.__VIEWSTATEGENERATOR,
            'from': 'http://so.gushiwen.org/user/collect.aspx',
            'email': 'wangjuchn@outlook.com',
            'pwd': 'zaijian211488',
            'code': code,
            'denglu': '登录'
        }
        response = self.s.post(url=url, headers=self.headers, data=formdata)
        with open("guishiwen.html", "w", encoding="utf8") as f:
            f.write(response.text)

    def run(self):
        self.dowmload_img()
        self.login()


def main():
    url = r'https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
    spider = SpiderSys(url, headers)
    spider.run()


if __name__ == '__main__':
    main()


