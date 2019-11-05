from PythonHTTP调用示例.打码兔 import YDMHttp

# 用户名
username    = 'snails'

# 密码
password    = 'zaijian211488'

# 软件ＩＤ，开发者分成必要参数。登录开发者后台【我的软件】获得！
appid       = 9357

# 软件密钥，开发者分成必要参数。登录开发者后台【我的软件】获得！
appkey      = '6b1a6a1add4ec8a979a7fd0c03db339f	'

# 图片文件
filename    = 'getimage.jpg'

# 验证码类型，# 例：1004表示4位字母数字，不同类型收费不同。请准确填写，否则影响识别率。在此查询所有类型 http://www.yundama.com/price.html
codetype    = 1004

# 超时时间，秒
timeout     = 60

# 检查
if (username == 'username'):
    print('请设置好相关参数再测试')
else:
    # 初始化
    yundama = YDMHttp(username, password, appid, appkey)

    # 登陆云打码
    uid = yundama.login();
    print('uid: %s' % uid)

    # 查询余额
    balance = yundama.balance();
    print('balance: %s' % balance)

    # 开始识别，图片路径，验证码类型ID，超时时间（秒），识别结果
    cid, result = yundama.decode(filename, codetype, timeout);
    print('cid: %s, result: %s' % (cid, result))

