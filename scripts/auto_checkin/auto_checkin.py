# -*- coding: utf-8 -*-

from urllib import request, parse
from urllib.error import HTTPError, URLError
from http import cookiejar
from os import system
from time import sleep
from datetime import datetime
from random import randint


def param_parser(file):
    '''
    Read username and password from config file.
    Return a dictionary which is just like:{username:password}

    '''
    dict = {}
    with open(file, encoding='UTF-8', mode='r') as f:
        for l in f.readlines():
            line = l.rstrip('\n').split(' ')
            dict[line[0]] = line[1]
    return dict


def url_builder(username, password):
    '''
    Build url using parameters username and password.

    '''
    u = parse.quote(username.encode('GBK'))
    p = password
    s = parse.quote('确认登录'.encode('GBK'))
    url = 'http://173.168.100.144/checklogin.jsp?username=' + u + '&password=' + p + '&Submit2=' + s
    return url


def send_request(url):
    """
    Build an opener with cookie support.
    Due to I don't know how to handle redirection responses, I just simply open several urls with one single
    opener as well as cookie it storage, and determine if those requests were correctly responsed by status code,
    then finally close it to release session.

    """
    # build opener
    cj = cookiejar.CookieJar()
    opener = request.build_opener(request.HTTPCookieProcessor(cj))
    # open homepage with opener and catch cookie
    r = opener.open('http://173.168.100.144/login.jsp')
    status1 = r.status
    # send login request with the opener containing cookie
    r = opener.open(url)
    status2 = r.status
    r = opener.open('http://173.168.100.144/attendance/checkin.jsp')
    status3 = r.status
    r = opener.open('http://173.168.100.144/index.jsp')
    status4 = r.status
    # close opener
    opener.close()
    return status1, status2, status3, status4


if __name__ == '__main__':
    try:
        dict = param_parser('config')
    except FileNotFoundError as e:
        print('config文件未找到！')
    else:
        for usr, pwd in dict.items():
            url = url_builder(usr, pwd)
            print('%s 正在签到......' % usr)
            try:
                status = send_request(url)
            except HTTPError as e:
                print('%s 签到失败！ 原因：用户名或密码错误。' % usr)
            except URLError as e:
                print('%s 签到失败！ 原因：网络连接错误。' % usr)
            else:
                if status == (200, 200, 200, 200):
                    time = datetime.now().strftime('%H:%M:%S')
                    print('%s 签到成功！签到时间：%s' % (usr, time))
                else:
                    print('%s 签到失败！' % usr, status)
                s = randint(1, 10)
                print('休息 %d 秒......' % s)
                sleep(s)

    finally:
        system('pause')
