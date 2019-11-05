from urllib import request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import re
import os


class SpiderPro(object):
    def __init__(self, start_url, path, page, proxy=None):
        self.start_url = start_url
        self.htmls = list()
        self.img_list = list()
        self.page = page
        self.count = 1
        self.proxy = proxy  # 这个ip和端口要换成可用的代理ip
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-gpu')
        if self.proxy is not None:
            chrome_options.add_argument('--proxy-server=http://' + self.proxy)

        self.browser = webdriver.Chrome(executable_path=path, options=chrome_options)
        # self.browser = webdriver.Chrome(executable_path=path)

    def get_page_source(self):
        self.browser.get(self.start_url)
        html = self.browser.page_source
        for page in range(self.page):

            self.htmls.append(html)
            next_page = self.browser.find_element_by_xpath('//div[@class="page"]/a[contains(text(), "下")]')
            next_page.click()
            html = self.browser.page_source
            time.sleep(2)
        self.browser.quit()

    def parse_html(self):
        for html_page in self.htmls:
            soup = BeautifulSoup(html_page, 'lxml')
            ret = soup.select(".list")[0]
            ret = str(ret.find_all('img'))
            self.img_list.extend(re.findall(r'src="(.*?jpg)"/>', ret))

    def download_img(self):
        dir_path = "image"
        if not os.path.exists(dir_path):
            if not os.path.isdir(dir_path):
                os.mkdir(dir_path)
        for img in self.img_list:
            image_name = os.path.basename(img)
            image_path = os.path.join(dir_path, image_name)
            try:
                print("第%d张开始下载" % self.count)
                request.urlretrieve(url=img, filename=image_path)
                print("第%d张结束下载" % self.count)
                self.count += 1
            except Exception as e:
                print(e)

    def run(self):
        self.get_page_source()
        self.parse_html()
        self.download_img()


def main(proxy=None):
    # proxy = '171.35.223.56:9999'  # 这个ip和端口要换成可用的代理ip
    # start_url = r'http://www.netbian.com/index.htm'
    print("请选择您想下载的图片类型：")
    print("日历：rili\t动漫：dongman\t风景：fengjing\n美女:meinv\t可爱:keai\t动物:dongwu")
    word = input("您想下载的图片类型：")
    page = int(input("您需要爬去多少页图片（一页18张）："))

    start_url = r'http://www.netbian.com/%s/' % word
    path = r'C:\Users\wangju\Desktop\Spider\chromedriver_win32\chromedriver.exe'
    spider_pro = SpiderPro(start_url, path, page, proxy)
    spider_pro.run()


if __name__ == '__main__':

    main()
