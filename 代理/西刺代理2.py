from bs4 import BeautifulSoup
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class GetIp(object):
    def __init__(self, url, path, page):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument('--disable-gpu')
        self.path = path
        self.items_list = list()
        self.flag = False
        self.url = url
        self.page = page

        self.browser = webdriver.Chrome(executable_path=self.path, options=self.chrome_options)

    def get_data(self):
        self.browser.get(self.url)
        for _ in range(self.page):
            time.sleep(2)
            self.content = self.browser.page_source
            self.parse_data()
            next_click = self.browser.find_elements_by_xpath(r'//div[@class="pagination"]/a[contains(text(), "下")]')[0]
            next_click.click()
        self.browser.quit()
        # print(self.content)

    # 利用bs4解析数据，返回列表[{'IP地址':117.26.44.147},{'端口':9999}...]
    def parse_data(self):
        soup = BeautifulSoup(self.content, 'lxml')
        ip_info_list = soup.select('table > tbody > tr')[1:]
        # print(ip_info_list)
        for ip_info in ip_info_list:
            ip_number = ip_info.find_all('td')[1].text
            # print(ip_number)
            ip_port = ip_info.find_all('td')[2].text
            # print(ip_port)
            ip_address = ip_info.find_all('td')[3].text.strip('\n')
            # print(ip_address)
            ip_anonymous = ip_info.find_all('td')[4].text
            # print(ip_anonymous)
            ip_type = ip_info.find_all('td')[5].text
            # print(ip_type)
            ip_life = ip_info.find_all('td')[8].text
            # print(ip_life)
            ip_time = ip_info.find_all('td')[-1].text
            # print(ip_time)
            item = {
                'IP地址': ip_number,
                '端口': ip_port,
                '服务地址': ip_address,
                '是否匿名': ip_anonymous,
                '类型': ip_type,
                '存活时间': ip_life,
                '验证时间': ip_time
            }
            self.items_list.append(item)
        # print(self.items_list)
        for i in self.items_list:
            print(i)

    def download_info(self):
        with open("ip_info.csv", "w", newline='') as f:
            res = csv.writer(f)
            if not self.flag:
                res.writerow(self.items_list[0].keys())
                self.flag = True
            for item in self.items_list:
                res.writerow(item.values())

    def run(self):
        self.get_data()
        self.download_info()


def main():
    page = int(input("你想爬取几页代理ip信息(一页100条)："))
    url = r'http://www.xicidaili.com/nn/'
    path = r'C:\Users\wangju\Desktop\Spider\chromedriver_win32\chromedriver.exe'
    insect = GetIp(url, path, page)
    insect.run()


if __name__ == '__main__':
    main()
