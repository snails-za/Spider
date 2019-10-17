import csv
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import time
from multiprocessing import Process
from multiprocessing import Queue


class QianChengSpider(object):
    def __init__(self, kw, start_page, end_page, headers):
        self.kw = kw
        self.start_page = start_page
        self.end_page = end_page
        self.headers = headers
        # 定义存放解析出来的工作信息的队列，用作两个进程之间的通信
        self.info_list = Queue()
        # 定义存放判断标志信息的队列，用作判断是否为第一页第一行
        self.flag = Queue()

    # 根据每页的page创建请求对象
    def handle_request(self, url):
        request = urllib.request.Request(url=url, headers=self.headers)
        return request

    # 解析内容
    def parse_content(self, content, page):
        print("第%d页数据开始解析。。。。。。" % page)
        # 生成对象
        soup = BeautifulSoup(content, 'lxml')
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
        print("第%d页数据结束解析。。。。。。" % page)

    def save_csv(self, page):
        time.sleep(0.5)
        print("第%d页数据开始下载。。。。。。" % page)
        info_start = None
        with open(self.kw + '.csv', "a", newline='') as fp:
            r = csv.writer(fp)
            # 判断是否为第一页第一行，为空则是，否则不是
            if not self.flag.qsize():
                info_start = self.info_list.get(True)
                r.writerow(info_start.keys())
                self.flag.put(1)
            # 获取第一页第一行的数据（工作信息）
            if info_start:
                r.writerow(info_start.values())
            for _ in range(self.info_list.qsize()):
                info = self.info_list.get(True)
                r.writerow(info.values())
        print("第%d页数据结束下载。。。。。。" % page)

    # 爬取程序
    def run(self):
        print("开始爬取数据。。。")
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
            content = str(response.read(), encoding='gb18030')
            time.sleep(1)
            # 创建进程
            # self.parse_content(content)
            p = Process(target=self.parse_content, args=(content, page))

            s = Process(target=self.save_csv, args=(page,))
            # 解析内容
            p.start()
            # 下载内容
            s.start()
            p.join()
            s.join()
        print("数据爬去完成。。。")

        # print("数据开始下载。。。。。。")
        # # 保存csv文件
        # self.save_csv()
        # print("数据结束下载。。。。。。")


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
        print(e)
        main()


if __name__ == "__main__":
    main()
