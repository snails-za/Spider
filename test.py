import csv
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import time
from multiprocessing import Pool
from multiprocessing import Queue


class QianChengSpider(object):
    def __init__(self, kw, start_page, end_page, headers):
        self.kw = kw
        self.start_page = start_page
        self.end_page = end_page
        self.headers = headers
        self.info_list = Queue()
        self.content = Queue()
        self._ = []
        self.p = Pool()

    # 根据每页的page创建请求对象
    def handle_request(self, url):
        request = urllib.request.Request(url=url, headers=self.headers)
        return request

    # 解析内容
    def parse_content(self):
        print("解析")
        # 生成对象
        soup = BeautifulSoup(self.content.get(), 'lxml')
        div_list = soup.select('#resultList')
        # div_list = div_list[4:]
        zwm_list = div_list[0].select('.el > .t1 > span')
        # print(len(zwm_list))
        gsm_list = div_list[0].select('.el > .t2 > a')
        # print(len(gsm_list))
        gzdd_list = div_list[0].select('.el > .t3')[1:]
        # print(len(gzdd_list))
        xz_list = div_list[0].select('.el > .t4')[1:]
        # print(len(xz_list))
        fbrq_list = div_list[0].select('.el > .t5')[1:]
        # print(len(fbrq_list))
        for zwm, gsm, gzdd, xz, fbrq in zip(zwm_list, gsm_list, gzdd_list, xz_list, fbrq_list):
            """
            items["职位名"] = zwm.text
            items["公司名"] = gsm.text
            items["工作地点"] = gzdd.text
            items["薪资"] = xz.text
            items["发布日期"] = fbrq.text

            错误：原因是字典有传递性，字典中的属性会自动改变（地址）
            """

            items = {
                "职位名": zwm.text,
                "公司名": gsm.text,
                "工作地点": gzdd.text,
                "薪资": xz.text,
                "发布日期": fbrq.text,
            }
            # print(items)
            self.info_list.put(items)
        # print(self.info_list)

    def save_csv(self):
        time.sleep(0.5)
        print("保存")
        info_start = None
        with open("jobs.csv", "a", newline='') as fp:
            r = csv.writer(fp)
            if not self._:
                info_start = self.info_list.get(True)
                r.writerow(info_start.keys())
                self._ = [1]
            for _ in range(self.info_list.qsize()):
                if info_start:
                    r.writerow(info_start.values())
                else:
                    info = self.info_list.get(True)
                    r.writerow(info.values())

    # 爬取程序
    def run(self):
        flag = False
        for page in range(self.start_page, self.end_page + 1):
            # https://search.51job.com/list/000000,000000,0000,00,9,99,c,2,1.html?
            url = r'https://search.51job.com/list/000000,000000,0000,00,9,99,{},2,{}.html?' \
                  r'lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&' \
                  r'companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&' \
                  r'dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(self.kw, page)

            # 创建请求对象
            request = self.handle_request(url)
            # 发送请求, 获取内容
            response = urllib.request.urlopen(request)
            self.content.put(str(response.read(), encoding='gb18030'))
            time.sleep(1)
            # 解析内容
            if not flag:
                self.p.apply_async(self.parse_content)
                self.p.apply_async(self.save_csv)
                flag = True







def main():
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
            'Accept': 'text/css,*/*;q=0.1',
            'Connection': 'keep - alive',

        }

        kw = input("请输入工作关键字：")
        start_page = int(input("请输入起始页码："))
        end_page = int(input("请输入结束页码："))

        # 创建对象，启动爬去程序
        spider = QianChengSpider(kw, start_page, end_page, headers)
        spider.run()

    except Exception as e:
        print("e")
        main()


if __name__ == "__main__":
    main()
