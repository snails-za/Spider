import urllib.request
import urllib.parse

url = r'http://www.renren.com/972450191/profile'

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',

        'Cookie': 'anonymid=k1lgsweri0u6vo; depovince=GW; jebecookies=53be24f6-6c48-4388-987c-cca496263f05|||||; _r01_=1; JSESSIONID=abcGMC0bIoQ1D5FzIE42w; ick_login=f2f5bc0b-fbd3-4a85-aa07-64c43e664b3d; t=01bd3459e6213d4a66705b12de731a231; societyguester=01bd3459e6213d4a66705b12de731a231; id=972450191; xnsid=478560dd; ver=7.0; loginfrom=null; jebe_key=cade7515-11e8-4ad4-bbd5-06e3b8a5b46f%7Cd92323ba45753b84fe1aa5048ac7af35%7C1570758109728%7C1%7C1570812168313; jebe_key=cade7515-11e8-4ad4-bbd5-06e3b8a5b46f%7Cd92323ba45753b84fe1aa5048ac7af35%7C1570758109728%7C1%7C1570812168318; wp_fold=0'

        }
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)

with open("renren.html", "wb") as fp:
    fp.write(response.read())


