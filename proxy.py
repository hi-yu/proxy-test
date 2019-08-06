#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : hiyu
# @Site    : iuiu.me
import urllib.request
inputurl = input('输入用代理访问的网站(注意要加上协议):')
url= '%s'%inputurl
time = int(input('访问时间限制（秒）：'))
tcp = input('输入访问使用的协议(http,https,sock5...):')
iplist = input('ip(如果多个使用使用分号";"隔开):').split(sep=';')
n = len(iplist)
print('共有%s个ip' % n)
a = -1
b = 0
while (a<n):
    a+=1
    b+=1
    if a==n:
        print('test over')
        break
    ip = iplist[a]
    proxy_support = urllib.request.ProxyHandler({'%s'%tcp:ip})
    opener = urllib.request.build_opener(proxy_support)
    opener.addheaders = [("User-Agent",'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')]
    urllib.request.install_opener(opener)
    try:
        print('正在测试第%s个ip,ip:%s ..'% (b,ip))
        response = urllib.request.urlopen(url,timeout=time)
    except Exception as e:
        print(str(e))#打印失败原因

    else:
        print('ok')
        f = open('proxy.txt', 'a')#在此.py相同目录下创建proxy.txt
        f.writelines(['%s\n'% ip])#写入可以使用的代理ip
        f.close()
        res_list = []
        f = open("proxy.txt", 'r')
        dup = []
        index = 0
        dul = open("okproxy.txt", 'w')
        for line in f.readlines():
            index = index + 1
            if line in res_list:
                print('in list')
            else:
                line.replace("\n", " ")
                dul.write(line)
                res_list.append(line)



