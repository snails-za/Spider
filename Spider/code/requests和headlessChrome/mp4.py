import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import os
import base64


class SpiderMovie(object):
    def __init__(self):
        self.se = requests.Session()
        self.index_url = r'https://www.365yg.com'
        self.headers = {
            # 'Host': 'www.365yg.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0',
            'Accept': 'text/javascript, text/html, application/xml, text/xml, */*',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Connection': 'keep-alive',
            'Referer': 'https://www.365yg.com/'

        }
        self.json_url = r'https://www.365yg.com/api/pc/feed/?min_behot_time=0&category=video_new&utm_source=toutiao&widen=1&tadrequire=true&as=A1955D1B344D2EE&cp=5DB46D82FECEFE1&_signature=KXfXpBAVdMuglu4-CnkOTil317'
        path = r'C:\Users\wangju\Desktop\Spider\chromedriver_win32\chromedriver.exe'
        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        self.browser = webdriver.Chrome(executable_path=path, options=chrome_options)
        self.get_src = r'<video class.*?src="(.*?)"></video>'

    def get_content(self):
        video_data = self.se.get(url=self.json_url, headers=self.headers).json()['data']
        for video_src in video_data:
            video_url = self.index_url + video_src['source_url']
            self.video_title = video_src['title']
            # print(video_url, self.video_title)
            self.browser.get(video_url)
            time.sleep(2)
            html = self.browser.page_source
            # print(html)
            self.parse_html(html)

    def parse_html(self, html):
        soup = BeautifulSoup(html, 'lxml')
        try:
            t = "https:" + str(soup.select('video')[0]["src"])
            print(t)
            self.save_file(t)

        except Exception as e:
            pass

    def save_file(self, t):
        r = self.se.get(url=t, headers=self.headers)
        video = r.content
        file_dir = "movie"
        if not os.path.exists(file_dir):
            if not os.path.isdir(file_dir):
                os.mkdir(file_dir)
        file_name = os.path.basename(self.video_title) + '.mp4'
        file_path = os.path.join(file_dir, file_name)
        with open(file_path, "wb") as f:
            f.write(video)

    def run(self):
        self.get_content()


def main():
    video_spider = SpiderMovie()
    video_spider.run()


if __name__ == '__main__':
    main()

