import requests

url = r'https://cn.bing.com/tlookupv3?isVertical=1&&IG=774820DAFF904CB7AEB6F1F63B50BB1F&IID=translator.5028.11'

word = input("请输入单词:")
form_data = {
    'from': 'en',
    'to': 'zh-Hans',
    'text': word
    }
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}

r = requests.post(url=url, headers=headers, data=form_data)
print(r.json())


