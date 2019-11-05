import requests
import threading
from queue import Queue
from bs4 import BeautifulSoup
import time
import csv

g_craw_list = list()

g_parse_list = list()


class CrawThread(threading.Thread):
    def __init__(self, page_queue, data_queue, lock):
        super().__init__()
        self.page_queue = page_queue
        self.data_queue = data_queue
        self.headers = {
            'Host': 'image.baidu.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
            'Accept': 'text/plain, */*; q=0.01',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'keep-alive',
            'Referer': 'https://image.baidu.com/search/index?tn=baiduimage&st=-1&ipn=r&ct=201326592&nc=1&lm=-1&cl=2&ie=utf-8&word=%E5%8A%A8%E7%89%A9&ie=utf-8&istype=2&fm=se0',
            'Cookie': 'BDqhfp=%E5%8A%A8%E7%89%A9%26%26NaN-1undefined-1undefined%26%264630%26%267; BAIDUID=04AF0E6FCEB74A3E6CA2C32606EF8892:FG=1; BIDUPSID=D8CAC45F89186CC0232016FF853C7430; PSTM=1557136117; BDUSS=RISjJMQkdvREJSdWo0V2VvQlJ6MElVQmNHd3diWDFycE5zdXJ3NmNIT0E3MXhkSVFBQUFBJCQAAAAAAAAAAAEAAAC5XwWb17fRsDE2NTEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIBiNV2AYjVddH; indexPageSugList=%5B%22dongwu%22%2C%22meinv%22%2C%22%E5%8A%A8%E7%89%A9%22%2C%22%E9%A3%8E%E6%99%AF%22%2C%22%E6%96%97%E9%B1%BC%22%5D; H_PS_PSSID=1426_21082_29721_29567_29221_22159; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDRCVFR[Hp1ap0hMjsC]=mk3SLVN4HKm; delPer=0; PSINO=1; BCLID=12201827791489652894; BDSFRCVID=F5LOJeC627Sm8SnwCqGkuuATumJVeXcTH6aIS-WX22TRn74wT44REG0P_M8g0KubTVMxogKKy2OTH9DF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tJkOoK0afC83qPbv-P4_5bLSMMnXKK62aKDsKD51BhcqEIL4jpbVehtH5PbD0-ntbm6nLR6FQJ5iHUbSj4Qz0IuiWaKHLpjXJbnf-I-2Lq5nhMJ3Xj7JDMP0-ROpWRvy523iXCovQpPBshQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xXj_0-nDSHHKDtj8t3e; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; firstShowTip=1; userFrom=www.baidu.com; cleanHistoryStatus=0',

        }
        self.url = r'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&'

        self.lock =lock

    def run(self):
        self.lock.acquire()
        print("爬取线程%s启动" % threading.current_thread().name)
        while not self.page_queue.empty():
            self.page_queue.get()
            print("11111111")
            print("22222222")
            print("333333333")
            print("444444444")
            self.data_queue.put(1)
        print("爬取线程%s结束" % threading.current_thread().name)
        self.lock.release()


class ParseThread(threading.Thread):
    def __init__(self, data_queue, lock, res):
        super().__init__()
        self.data_queue = data_queue
        self.lock = lock

    def run(self):
        time.sleep(1)
        self.lock.acquire()
        print("解析线程%s启动" % threading.current_thread().name)
        while not self.data_queue.empty():
            self.data_queue.get()
            print("aaaaa")
            print("bbbbb")
            print("cccccc")
            print("eeeeee")
        print("解析线程%s结束" % threading.current_thread().name)
        self.lock.release()


def create_queue():
    # 创建页码队列
    page_queue = Queue()
    for page in range(1, 80):
        page_queue.put(page)
    # 创建内容队列
    data_queue = Queue()
    return page_queue, data_queue


def create_crawl_thread(page_queue, data_queue, lock):
    for _ in range(2):
        tcraw = CrawThread(page_queue, data_queue, lock)
        g_craw_list.append(tcraw)


def create_parse_thread(data_queue, lock, res):
    for _ in range(2):
        tparse = ParseThread(data_queue, lock, res)
        g_parse_list.append(tparse)


def main():
    print("主进程开始了。。。。。")
    with open("ip_info.csv", "w", newline='') as f:
        res = csv.writer(f)
    # 创建锁
    lock1 = threading.Lock()
    lock2 = threading.Lock()
    # 创建队列
    page_queue, data_queue = create_queue()
    # 创建爬取线程
    create_crawl_thread(page_queue, data_queue, lock1)
    # 创建解析线程
    create_parse_thread(data_queue, lock2, res)
    # 进程开始
    for craw, parse in zip(g_craw_list, g_parse_list):
        craw.start()
        parse.start()
    for craw, parse in zip(g_craw_list, g_parse_list):
        craw.join()
        parse.join()
    print("主进程结束了。。。。。")


if __name__ == '__main__':
    main()



