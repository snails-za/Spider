import requests
import threading
from queue import Queue
import time
from lxml import etree

g_items = list()


class ParseThread(threading.Thread):
    def __init__(self, data_queue):
        super().__init__()
        self.data_queue = data_queue

    def run(self):
        time.sleep(1)
        print("解析线程%s启动" % threading.current_thread().name)
        text = self.data_queue.get()
        items = self.parse_text(text)
        print("解析线程%s结束" % threading.current_thread().name)

    def parse_text(self, text):
        tree = etree.HTML(text)
        img_list = tree.xpath(
            r'//div[@class="list_cont list_cont2 w1180"]//ul[@class="clearfix"]//li//img/@src')
        title_list = tree.xpath(
            r'//div[@class="list_cont list_cont2 w1180"]//ul[@class="clearfix"]//li//img/@title')
        # print(img_list)
        # print(title_list)
        for img, title in zip(img_list, title_list):

            item = {
                "img": img,
                "title": title
            }
            g_items.append(item)
        print(len(g_items))


class DownloadThread(threading.Thread):
    def __init__(self, data_queue):

        super().__init__()
        self.data_queue = data_queue

    def run(self):
        time.sleep(3)
        if g_items:
            print("下载线程%s启动" % threading.current_thread().name)
            for img in g_items:
                with open('image' + '/' + img["title"] + '.jpg', "wb") as f:
                    r = requests.get(url=img["img"])
                    f.write(r.content)

        print("下载线程%s结束" % threading.current_thread().name)

def create_queue():
    # 创建内容队列
    data_queue = Queue()
    return data_queue


def create_parse_thread(data_queue):
    tparse = ParseThread(data_queue)
    return tparse


def create_download_thread(data_queue):
    tdown = DownloadThread(data_queue)
    return tdown


def craw_thread(data_queue):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',}
    url = r'http://www.win4000.com/mobile.html'

    response = requests.get(url=url, headers=headers)
    data_queue.put(response.text)


def main():
    print("主进程开始了。。。。。")
    data_queue = create_queue()
    craw_thread(data_queue)
    # 创建解析线程
    tparse = create_parse_thread(data_queue)
    # 创建抓取线程
    tdown = create_download_thread(data_queue)
    # 启动线程
    tparse.start()
    tdown.start()
    tparse.join()
    tdown.join()
    print("主进程结束了。。。。。")


if __name__ == '__main__':
    main()



