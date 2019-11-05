import urllib.request
import urllib.parse
from lxml import etree
import json


def handle_request(url, headers, page):
    data = {"page": page}
    data = urllib.parse.urlencode(data)
    url_now = url + data
    request = urllib.request.Request(url=url_now, headers=headers)
    content = urllib.request.urlopen(request).read().decode()
    return content


def analyse_content(content):
    # 生成对象
    tree = etree.HTML(content)
    # passage_list = tree.xpath(r'/html/body/div[1]/div[8]/div[2]/div[2]/div/p/a/text()')
    # for passage in passage_list:
    #     print(passage)
    odiv = tree.xpath(r'/html/body/div[1]/div[8]/div[2]/div[2]')[0]
    passage_list = odiv.xpath(r'//div/p/a/text()')
    # for passage in passage_list:
    #     print(passage)
    return passage_list


def save_file(passage_list):
    with open("duanzi.txt", "a", encoding="utf8") as f:
        for passage in passage_list:
            # print(passage)
            dict1 = {"passage": passage}
            string = json.dumps(dict1, ensure_ascii=False)
            # print(string)
            # json.dump(dict1, f, ensure_ascii=False)
            f.write(string)


def main():
    start_page = int(input("开始页码："))
    end_page = int(input("结束页码："))
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
    url = r'https://www.xiaohua.com/duanzi?'
    for page in range(start_page, end_page + 1):
        content = handle_request(url, headers, page)
        # print(content)
        passage_list = analyse_content(content)
        save_file(passage_list)


if __name__ == '__main__':
    main()



