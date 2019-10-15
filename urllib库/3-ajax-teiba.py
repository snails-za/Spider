import urllib.request
import urllib.parse
import os

ba_name = input("请输入吧名：")

start_page = int(input("请输入起始页码："))
end_page = int(input("请输入要爬取的结束页码："))

# 创建文件夹
if not os.path.exists(ba_name):
    os.mkdir(ba_name)

for page in range(start_page, end_page + 1):
    
    url = r'http://tieba.baidu.com/f?'
    data = {
            'kw': ba_name,
            'ie': 'utf-8',
            'pn': str((page - 1) * 50)
            }

    headers = {
            'Host': 'tieba.baidu.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Connection': 'keep-alive',
            'Cookie': 'BAIDUID=04AF0E6FCEB74A3E6CA2C32606EF8892:FG=1; BIDUPSID=D8CAC45F89186CC0232016FF853C7430; PSTM=1557136117; BDUSS=RISjJMQkdvREJSdWo0V2VvQlJ6MElVQmNHd3diWDFycE5zdXJ3NmNIT0E3MXhkSVFBQUFBJCQAAAAAAAAAAAEAAAC5XwWb17fRsDE2NTEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIBiNV2AYjVddH; TIEBAUID=5a13ed663e5f49dda2da110c; TIEBA_USERTYPE=7b00a4222b85b84a1b9270d6; bdshare_firstime=1567987337601; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1567987338; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; STOKEN=aabf886c7b1af17a90a661b3e1c9c1c9497d6894fe159ee122f550637403c471; BDRCVFR[Hp1ap0hMjsC]=mk3SLVN4HKm; delPer=0; PSINO=1; H_PS_PSSID=1426_21082_29567_29221_22159; 2600820665_FRSVideoUploadTip=1',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0'

            }
    data = urllib.parse.urlencode(data)
    url += data
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)

    
    # 创建文件
    filename = ba_name + "_" + str(page) +".html"
    filepath = os.path.join(ba_name, filename)
    print("第%d页开始下载" % page)
    with open(filepath, "wb") as f:
        f.write(response.read())


    print("第%d页结束下载" % page)
