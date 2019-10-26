import requests


def main():
    # 如果碰到会话相关的问题，要首先创建一个会话
    # 往下所有的操作都通过s进行访问，s.get    s.post
    S = requests.Session()
    post_url = r'http://www.renren.com/ajaxLogin/login?1=1&'
    post_headers = {
        # 'Host': 'www.renren.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
        # 'Content-Type': 'application/x-www-form-urlencoded',
        # 'X-Requested-With': 'XMLHttpRequest',
        # 'Content-Length': '256',
        # 'Connection': 'keep-alive',
        # 'Referer': 'http://www.renren.com/SysHome.do?origURL=http%3A%2F%2Fwww.renren.com%2F972455360%2Fnewsfeed%2Fphoto',
        # 'Cookie': 'anonymid=k1lgsweri0u6vo; _r01_=1; jebe_key=cade7515-11e8-4ad4-bbd5-06e3b8a5b46f%7Cec3260df92916c9b53da6bef5682d969%7C1570852619499%7C1%7C1570906678797; jebe_key=cade7515-11e8-4ad4-bbd5-06e3b8a5b46f%7Cec3260df92916c9b53da6bef5682d969%7C1570852619499%7C1%7C1571977776926; _de=5BFA36E710422D3B070BF98752FC884D; ln_uact=15829377201; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; depovince=GW; jebecookies=6232626e-dc4d-4b17-91f2-779f69a552fa|||||; JSESSIONID=abcwDo7WnTq1oaR0F893w; ick_login=0d50b63a-fd26-43db-b8be-f50f5bf80959; first_login_flag=1; societyguester=0c52a1863d43dc33cf05a5b8785042f90; id=972455360; xnsid=20ba230; loginfrom=null; ver=7.0; wp_fold=0',
    }
    formdata = {
        'email': '15829377201',
        'icode': '',
        'origURL': 'http://www.renren.com/home',
        'domain': 'renren.com',
        'key_id': '1',
        'captcha_type': 'web_login',
        'password': '511154fe965841a00ee5b6aa6e938757aec8699f03b3dde2b1241f03f90f6c92',
        'rkey': '33c14357d55b6ff027dcd56e46cb529e',
        'f': 'http%3A%2F%2Fwww.renren.com%2F972455360%2Fnewsfeed%2Fphoto'
    }
    r = S.post(url=post_url, headers=post_headers, data=formdata)
    print(r.text)
    get_url = r'http://www.renren.com/972455360/profile HTTP/1.1'
    t = S.get(url=get_url, headers=post_headers)
    print(t.text)


if __name__ == '__main__':
    main()
