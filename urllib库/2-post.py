import urllib.request
import urllib.parse


post_url = r'https://fanyi.baidu.com/v2transapi?from=en&to=zh '
word = input("请输入你想查询的单词：")


# 构建表单数据
form_data = {
        'from':	'en',
        'to': 'zh',
        'query': word,
        'transtype': 'realtime',
        'simple_means_flag': '3',
        'sign':	'814534.560887',
        'token': '4993c641ac43fcca6c11214ac70cee14'
        }

 
# 创建请求对象
headers = {
        'Host': 'fanyi.baidu.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        # 'Content-Length': '121',
        'Connection': 'keep-alive',
        'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
        'Cookie': 'BAIDUID=04AF0E6FCEB74A3E6CA2C32606EF8892:FG=1; BIDUPSID=D8CAC45F89186CC0232016FF853C7430; PSTM=1557136117; BDUSS=RISjJMQkdvREJSdWo0V2VvQlJ6MElVQmNHd3diWDFycE5zdXJ3NmNIT0E3MXhkSVFBQUFBJCQAAAAAAAAAAAEAAAC5XwWb17fRsDE2NTEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIBiNV2AYjVddH; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; pgv_pvi=7097348096; BDRCVFR[Hp1ap0hMjsC]=mk3SLVN4HKm; delPer=0; PSINO=1; H_PS_PSSID=1426_21082_29522_29567_29221_22159; locale=zh; yjs_js_security_passport=3cd910cbc128a631117080c279c52a89ce8c03f1_1570513959_js; __yjsv5_shitong=1.0_7_fee61c38718c354c7243b1691cb21139ba55_300_1570513955446_111.19.99.34_4d680d48',

        }

request = urllib.request.Request(url=post_url, headers=headers)

# 发送请求
form_data = urllib.parse.urlencode(form_data).encode()
response = urllib.request.urlopen(request, form_data)


# 打印结果
print(response.read().decode())
