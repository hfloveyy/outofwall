#!/usr/bin/env python
# coding=utf-8
import requests
from bs4 import BeautifulSoup
import re
import subprocess

banner ='''

 #    #  ######  #        ####   #    #  ######   #   #   #   #
 #    #  #       #       #    #  #    #  #         # #     # #
 ######  #####   #       #    #  #    #  #####      #       #
 #    #  #       #       #    #  #    #  #          #       #
 #    #  #       #       #    #   #  #   #          #       #
 #    #  #       ######   ####     ##    ######     #       #
'''


def get_url_and_password(content):
    soup = BeautifulSoup(content)
#    print type(soup.find_all(id ='free'))
#    print soup.find_all(text=re.compile(u'A服务器地址'))
    urladdr = str(soup.find_all(text=re.compile(u'A服务器地址')))
    port = str(soup.find_all(text=re.compile(u'端口')))
    password = str(soup.find_all(text=re.compile(u'A密码')))
    addr = urladdr[-12:-2]
    password = password[-10:-2]
    #print addr
    #print password
    args = 'sslocal  -p 443 -b 127.0.0.1 -l 1080  -t 600 -m aes-256-cfb -s '+addr+' -k '+password
    print banner
    print u'开启科学上网！'
    print u'设置浏览器代理(firefox:autoproxy,chrome:SwitchyOmega) IP=127.0.0.1 端口：1080'
   # for line in p.stdout.readlines():
    #    print line,
    try:
        p = subprocess.Popen(args, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        retval = p.wait()
    except KeyboardInterrupt:
        print u'退出！'


r = requests.get('http://www.ishadowsocks.com')
get_url_and_password(r.content)
