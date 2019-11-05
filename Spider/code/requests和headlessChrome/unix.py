import requests
from bs4 import BeautifulSoup
from PythonHTTP调用示例.打码兔 import YDMHttp


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
        with open("imgCode.jpg", "wb") as f:
            f.write(img_n.content)
        # 获取类似cookie之类的验证信息参数
        self.__VIEWSTATE = soup.find("input", id="__VIEWSTATE")['value']
        self.__VIEWSTATEGENERATOR = soup.find("input", id="__VIEWSTATEGENERATOR")['value']
        # print(self.__VIEWSTATE)
        # print(self.__VIEWSTATEGENERATOR)

    def get_code(self):
        # 用户名
        username = 'snails'

        # 密码
        password = 'zaijian211488'

        # 软件ＩＤ，开发者分成必要参数。登录开发者后台【我的软件】获得！
        appid = 9357

        # 软件密钥，开发者分成必要参数。登录开发者后台【我的软件】获得！
        appkey = '6b1a6a1add4ec8a979a7fd0c03db339f	'

        # 图片文件
        filename = 'imgCode.jpg'

        # 验证码类型，# 例：1004表示4位字母数字，不同类型收费不同。请准确填写，否则影响识别率。在此查询所有类型 http://www.yundama.com/price.html
        codetype = 1004

        # 超时时间，秒
        timeout = 60

        # 检查
        if (username == 'username'):
            print('请设置好相关参数再测试')
        else:
            # 初始化
            yundama = YDMHttp(username, password, appid, appkey)

            # 登陆云打码
            uid = yundama.login()
            print('uid: %s' % uid)

            # 查询余额
            balance = yundama.balance()
            print('balance: %s' % balance)

            # 开始识别，图片路径，验证码类型ID，超时时间（秒），识别结果
            cid, result = yundama.decode(filename, codetype, timeout)
            print('cid: %s, result: %s' % (cid, result))
            return result

    def login(self, code):
        url = r'https://so.gushiwen.org/user/login.aspx?from=http%3a%2f%2fso.gushiwen.org%2fuser%2fcollect.aspx'
        # 提示用户输入验证码
        # code = input("请输入验证码：")
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
        code = self.get_code()
        self.login(code)


def main():
    url = r'https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
    spider = SpiderSys(url, headers)
    spider.run()


if __name__ == '__main__':
    main()


