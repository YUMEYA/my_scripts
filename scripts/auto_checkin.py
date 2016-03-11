from urllib import request, parse
from urllib.error import HTTPError, URLError
from http import cookiejar


def param_parser(file):
    line = []
    dict = {}
    with open(file, encoding='UTF-8', mode='r') as f:
        for l in f.readlines():
            line = l.rstrip('\n').split(' ')
            dict[line[0]] = line[1]
    return dict


def url_builder(username, password):
    u = parse.quote(username.encode('GBK'))
    p = password
    s = parse.quote('确认登录'.encode('GBK'))
    url = 'http://173.168.100.144/checklogin.jsp?username=' + u + '&password=' + p + '&Submit2=' + s
    return url


def send_request(url):
    cj = cookiejar.CookieJar()
    opener = request.build_opener(request.HTTPCookieProcessor(cj))
    r = opener.open('http://173.168.100.144/login.jsp')
    status1 = r.status
    r = opener.open(url)
    status2 = r.status
    r = opener.open('http://173.168.100.144/index.jsp')
    status3 = r.status
    opener.close()
    return status1, status2, status3


if __name__ == '__main__':
    dict = param_parser('config')
    for usr, pwd in dict.items():
        url = url_builder(usr, pwd)
        try:
            status = send_request(url)
        except HTTPError as e:
            print('%s 签到失败！ 原因：用户名或密码错误。' % (usr))
        except URLError as e:
            print('%s 签到失败！ 原因：网络连接错误。' % (usr))
        else:
            if status == (200, 200, 200):
                print('%s 签到成功！' % usr)
