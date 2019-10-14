import urllib.request
import urllib.parse
import re

def handle_request(url, page=None):
    if page:
        url = url + str(page) + '.html'
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
            }
    request = urllib.request.Request(url=url, headers=headers)
    return request


def parse_content(content):
    get_url = r'<a href="(/lizhi/.*?)"><b>.*?</b>'
    get_neirong = r'<a href="/lizhi/.*?"><b>(.*?)</b>'
    get_neirong = re.findall(get_neirong, content)
    # get_neirong = re.sub(r'<img .*?>', '', get_neirong)
    get_url = re.findall(get_url, content)
    
    return get_neirong, get_url


def get_content(url):
    request = handle_request(url) 
    content = urllib.request.urlopen(request).read().decode()
    neirong = r'<div class="neirong">(.*?)</div>'
    # neirong = r'<ol class=" list-paddingleft-2" style=".*?">(.*?)</ol>'
    neirong = re.findall(neirong, content, re.S)
    neirong = re.sub(r'<img .*?>', '', neirong[0])
    return neirong


def save_file(string):
    with open("lizhi.html", "a") as f:
        f.write(string)


def main():
    url = r'http://www.yikexun.cn/lizhi/qianming/list_50_'
    start_page = int(input("请输入起始页码："))
    end_page = int(input("请输入结束页码："))

    for page in range(start_page, end_page):

        request = handle_request(url, page)
        content = urllib.request.urlopen(request).read().decode()
        get_neirong, get_url = parse_content(content)
        for link, title in zip(get_url, get_neirong):
            url = r'http://www.yikexun.cn'
            url += link
            neirong = get_content(url)
            string = '<h1>{}</h1>{}'.format(title, neirong)
            save_file(string)

if __name__ == "__main__":
    main()
