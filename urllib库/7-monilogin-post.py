import urllib.request
import urllib.parse
import http.cookiejar


# 真实的模拟浏览器，党法送完post请求的的时候，将cookie保存到代码中
# 创建一个cookiejar对象
cj = http.cookiejar.CookieJar()
# 通过cookiejar创建一个handler
handler = urllib.request.HTTPCookieProcessor(cj)
# 根据handler创建一个opener
opener = urllib.request.build_opener(handler)

post_url = r'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=201996102233'

form_data = {
        'email': '15829377201',
        'icode': '',	
        'origURL': 'http://www.renren.com/home',
        'domain': 'renren.com',
        'key_id': '1',
        'captcha_type':	'web_login',
        'password': '1393c9d3f5693cd73aed2d40bf3c259ce0e880f6c97c4fd2d8f42c60a8f25409',
        'rkey': '19f0ac391287a44a787df705b669e39d',
        'f': 'https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dpw1jYZXI6lI_xrkNz_NwztjBeaNu4HucCUTG16Fbj2a%26wd%3D%26eqid%3D8b5153d200033ec6000000035da13ccf'
        }

headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
        }


request = urllib.request.Request(url=post_url, headers=headers)

form_data = urllib.parse.urlencode(form_data).encode()

response = opener.open(request, data=form_data)

print(response.read().decode())

print("*" * 50)


get_url = r'http://www.renren.com/972455360/profile'

request = urllib.request.Request(url=get_url, headers=headers)

response = opener.open(request)

print(response.read().decode())

