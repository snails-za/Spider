import requests
from bs4 import BeautifulSoup
import csv

class GetIp(object):
    def __init__(self, url, headers, page):
        self.url = url
        self.headers = headers
        self.items_list = list()
        self.flag = False
        self.page = page

    def get_data(self):
        for i in range(1, self.page + 1):
            url = self.url + str(i)
            response = requests.get(url=url, headers=self.headers)
            self.content = response.text
            self.parse_data()
        # print(content)

    # 利用bs4解析数据，返回列表[{'IP地址':117.26.44.147},{'端口':9999}...]
    def parse_data(self):
        soup = BeautifulSoup(self.content, 'lxml')
        ip_info_list = soup.select('#ip_list > tr')[1:]
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
        print(len(self.items_list))
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
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'If-None-Match': 'W/"115b4622f6ed1f18d780eaaa5a3e3825"',
    'Cache-Control': 'max-age = 0',
}
    insect = GetIp(url, headers, page)
    insect.run()


if __name__ == '__main__':
    main()