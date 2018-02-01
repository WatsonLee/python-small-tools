# coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

import cookielib
import urllib2
import urllib
import requests
import json
from bs4 import BeautifulSoup

def test3():

    crack_url = "http://www.hashkill.com/c.php"
    cracko_url = "http://www.hashkill.com/co.php"

    proxies = {"http": "127.0.0.1:8888"}
    proxy_s = urllib2.ProxyHandler(proxies)
    p_opener = urllib2.build_opener(proxy_s)
    urllib2.install_opener(p_opener)

    cj = cookielib.CookieJar()
    cj_opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    #urllib2.install_opener(cj_opener)
    res = cj_opener.open("http://www.baidu.com")





    response = urllib2.urlopen("http://www.hashkill.com")
    soup = BeautifulSoup(response.content, "html.parser")
    input_lc = soup.find(attrs={"id": "__lc__"})

    data = {
        'userinfo': '',
        'h': "b497246667e4742e9889dc0750c6a125",
        'ht': "md5",
        'lc': input_lc["value"],
        'ct': "0",
        'aj': "0"
    }

    headers = {"Accept-Encoding":"gzip, deflate",
               "Accept-Language":"zh-CN,zh;q=0.8",
               "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4549.400 QQBrowser/9.7.12900.400",
               "Referer":"http://www.hashkill.com/",
               "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
               "Accept":"application/json, text/javascript, */*; q=0.01",
               "X-Requested-With":"XMLHttpRequest",
               "Connection":"keep-alive",
               "Host":"http://www.hashkill.com",
               "Origin":"http://www.hashkill.com"}

    reqo = urllib2.Request(cracko_url, headers=headers,data=urllib.urlencode({'action': 'checkAction', 'jyz': 'F'}))
    responseo = urllib2.urlopen(reqo)
    print responseo.read()

    encode_value = "userinfo=&h=b3df287bfaa7f1ce9e3a29ccda6787261529c76dcfa0a3884d41f1df785b84b2&ht=md5&lc=%s&ct=0&aj=0"%(input_lc["value"])
    req = urllib2.Request(crack_url, headers=headers, data=encode_value)
    response = urllib2.urlopen(req)
    print response.read()

def getcookie():
    #request = urllib2.Request("http://www.hashkill.com")
    sock = urllib2.urlopen("http://www.hashkill.com")
    cookies = sock.info()['Set-Cookie']
    for item in cookies:
        print "Name = %s\nValue = %s\n"%(item.name, item.value)

getcookie()
