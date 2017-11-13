import configparser
import requests
import hashlib
config = configparser.ConfigParser()
url = 'http://net.tsinghua.edu.cn/do_login.php'
config.read('conf.ini')

username = config["SETTING"]['username']
password = config["SETTING"]['password']

if username=='' or password=='':
	print('Failed to load setting')
	exit()
check_online = requests.post(url, {'action': 'check_online'})
if check_online.content != b'online':
    md5 = hashlib.md5()
    md5.update(password.encode('utf8'))
    print(md5.hexdigest())
    login = requests.post(url,
                          {
                              'action': 'login',
                              'username': username,
                              'password': '{MD5_HEX}' + md5.hexdigest(),
                              'ac_id': 1
                          })
    if login.content == b'E2553: Password is error.':
        print('Login Failed, Check Password or file encodeing')
    else:
        print('Login Success')
else:
	print('You are online')