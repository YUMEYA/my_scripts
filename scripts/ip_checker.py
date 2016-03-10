import os
import re


def execute_cmd(cmd):
    r = os.popen(cmd).read()
    return r


def extract_data(text):
    r = re.search('(丢失 = )\w{1}', text)
    t = str(r.group(0))
    s = int(t[5])
    return s


def gen_cmd(ip):
    cmd = 'ping ' + ip + ' -n 1'
    return cmd


def gen_ip_table():
    list = []
    for i in range(2, 127):
        list.append('10.2.24.' + str(i))
    return list

if __name__ == '__main__':
    print('processing...')

    ip_table = gen_ip_table()

    for ip in ip_table:
        output = execute_cmd(gen_cmd(ip))
        data = extract_data(output)
        if data == 1:
            print(ip + ' is available!')
        else:
            continue

    print('finish!')

    os.system('pause')
