#coding: utf-8

import urllib2
import urllib
import cookielib
import requests
from bs4 import BeautifulSoup

HOST = "http://www.hashkill.com"
HOST_CO = "http://www.hashkill.com/co.php"
HOST_C = "http://www.hashkill.com/c.php"

#def Crack():
#
#
#    #proxies = {"http": "127.0.0.1:8888"}
#    #proxy_s = urllib2.ProxyHandler(proxies)
#    #p_opener = urllib2.build_opener(proxy_s)
#    #urllib2.install_opener(p_opener)
#
#    host_headers = {
#        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4549.400 QQBrowser/9.7.12900.400",
#        "Accept-Language":"zh-CN,zh;q=0.8",
#        "Accept-Encoding":"gzip, deflate, sdch",
#        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#        "Cache-Control":"max-age=0",
#        "Referer":HOST,
#        "Host":HOST,
#        "Connection":"keep-alive"
#    }
#    cookies = dict(cookies_are='working')
#    res = requests.get(HOST, headers = host_headers, cookies = cookies)
#    print res.text
#    #cookies = res.cookies
#    print cookies
#
#
#    #soup = BeautifulSoup(response, "html.parser")
#    #input_lc = soup.find(attrs={"id":"__lc__"})["value"]
##
#    #data = {
#    #    'userinfo': '',
#    #    'h': "b497246667e4742e9889dc0750c6a125",
#    #    'ht': "md5",
#    #    'lc': input_lc,
#    #    'ct': "0",
#    #    'aj': "0"
#    #}
##
#    #headers = {"Accept-Encoding": "gzip, deflate",
#    #           "Accept-Language": "zh-CN,zh;q=0.8",
#    #           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4549.400 QQBrowser/9.7.12900.400",
#    #           "Referer": HOST,
#    #           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
#    #           "Accept": "application/json, text/javascript, */*; q=0.01",
#    #           "X-Requested-With": "XMLHttpRequest",
#    #           "Connection": "keep-alive",
#    #           "Host": HOST,
#    #           "Origin": HOST}
##
##
##
#    #req_co = urllib2.Request(HOST_CO,data=urllib.urlencode({'action': 'checkAction', 'jyz': 'F'}))
#    #response_co = urllib2.urlopen(req_co)
#    #print response_co.read()
##
#    ##urllib2.install_opener(opener)
#    #req = urllib2.urlopen(HOST_C, data= urllib.urlencode(data))
#    ##response = urllib2.urlopen(req)
##
#    #print req.read()
#
#def Crack1():
#
#    response = requests.get(HOST)
#    soup = BeautifulSoup(response.content, "html.parser")
#    input_lc = soup.find(attrs={"id": "__lc__"})
#    cookies = response.cookies
#
#    #cookies = "incap_ses_460_1051962=QyI4XgEALw8FcBPqeEBiBkrccVoAAAAAXdbmAVbiKZ9JT/wXjf7zAg==; PHPSESSID=ha2moacaqdlg17kj0unjoirk05; incap_ses_434_1051962=GN12PGGPC1R1WUiG++AFBoKjcloAAAAAL2KkwjGuzJ1U8jRJ8JubjQ==; visid_incap_1051962=PcCZpKKpSiqmZet1ZS+pZ5HVOVoAAAAAQUIPAAAAAAA9/L8HImzpSyUZ3XRHXZLe; incap_ses_894_1051962=W8erS+HUQhl/0U+uaCBoDKakcloAAAAAjk1Kl5bZz2XFWo73DDjTUg==; visid_incap_1165968=Nv8mXxZUSnGlMCKWkJujXwd1O1oAAAAAQUIPAAAAAAAZDccytpRwMRhlF9jWDTQl; incap_ses_463_1165968=2FivO8Cs6mZln+Xn2OhsBhm7c1oAAAAA/GrjQfBzDu7XnzPsN6iSIQ==; Hm_lvt_618db4f3d170d9404c3158f7c432e2c9=1517295410,1517376852,1517378074,1517454551; Hm_lpvt_618db4f3d170d9404c3158f7c432e2c9=1517536971"
#    opener = urllib2.build_opener()
#    opener.addheaders.append(("Cookie","cookiename="+cookies))
#    res0 = opener.open(HOST_CO,data=urllib.urlencode({'action': 'checkAction', 'jyz': 'F'}))
#
#    data = {
#        'userinfo': '',
#        'h': "b497246667e4742e9889dc0750c6a125",
#        'ht': "md5",
#        'lc': input_lc["value"],
#        'ct': "0",
#        'aj': "0"
#    }
#
#    headers = {"Accept-Encoding":"gzip, deflate",
#               "Accept-Language":"zh-CN,zh;q=0.8",
#               "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4549.400 QQBrowser/9.7.12900.400",
#               "Referer":"http://www.hashkill.com/",
#               "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
#               "Accept":"application/json, text/javascript, */*; q=0.01",
#               "X-Requested-With":"XMLHttpRequest",
#               "Connection":"keep-alive",
#               "Host":"http://www.hashkill.com",
#               "Origin":"http://www.hashkill.com"}
#
#
#
#    cookies = "incap_ses_460_1051962=QyI4XgEALw8FcBPqeEBiBkrccVoAAAAAXdbmAVbiKZ9JT/wXjf7zAg==; PHPSESSID=ha2moacaqdlg17kj0unjoirk05; incap_ses_434_1051962=GN12PGGPC1R1WUiG++AFBoKjcloAAAAAL2KkwjGuzJ1U8jRJ8JubjQ==; visid_incap_1051962=PcCZpKKpSiqmZet1ZS+pZ5HVOVoAAAAAQUIPAAAAAAA9/L8HImzpSyUZ3XRHXZLe; incap_ses_894_1051962=W8erS+HUQhl/0U+uaCBoDKakcloAAAAAjk1Kl5bZz2XFWo73DDjTUg==; visid_incap_1165968=Nv8mXxZUSnGlMCKWkJujXwd1O1oAAAAAQUIPAAAAAAAZDccytpRwMRhlF9jWDTQl; incap_ses_463_1165968=2FivO8Cs6mZln+Xn2OhsBhm7c1oAAAAA/GrjQfBzDu7XnzPsN6iSIQ==; Hm_lvt_618db4f3d170d9404c3158f7c432e2c9=1517295410,1517376852,1517378074,1517454551; Hm_lpvt_618db4f3d170d9404c3158f7c432e2c9=1517536971"
#    opener1 = urllib2.build_opener()
#
#    #opener1.addheaders = [("Accept-Encoding","gzip, deflate")]
#    opener1.addheaders = [
#        ("Accept-Language", "zh-CN,zh;q=0.8"),
#        ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4549.400 QQBrowser/9.7.12900.400"),
#        ("Referer", HOST),
#        ("Origin", HOST),
#        ("HOST", HOST),
#        ("Accept-Encoding", "gzip, deflate"),
#        ("Content-Type","application/x-www-form-urlencoded; charset=UTF-8"),
#        ("X-Requested-With","XMLHttpRequest"),
#        ("Accept","application/json, text/javascript, */*; q=0.01")
#
#    ]
#    #opener1.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4549.400 QQBrowser/9.7.12900.400")]
#    #opener1.addheaders = [("Referer",HOST)]
#    #opener1.addheaders = [("Origin", HOST)]
#    #opener1.addheaders = [("HOST", HOST)]
#    opener1.addheaders.append(("Cookie", "cookiename=" + cookies))
#    res1 = opener1.open(HOST_C, data=urllib.urlencode(data))
#    print res1.read()

def TransCookie(cookie):
    res = ""
    for name, value in cookie.iteritems():
        res+="%s=%s;"%(name,value)
    return res.rstrip(";")

def Crack2(hash_text):
    proxies = {
        "http": "http://127.0.0.1:8888"
    }



    session = requests.Session()
    response = session.get(HOST, proxies=proxies)
    soup = BeautifulSoup(response.content, "html.parser")
    input_lc = soup.find(attrs={"id":"__lc__"})["value"]
    print input_lc
    print session.cookies.get_dict()

    req_co = requests.Request("POST", HOST_CO, data={'action': 'checkAction', 'jyz': 'F'})
    resp_co = session.send(session.prepare_request(req_co), proxies=proxies)
    print resp_co.content


    data = {
        'userinfo': '',
        'h': "b497246667e4742e9889dc0750c6a125",
        'ht': "md5",
        'lc': input_lc,
        'ct': "0",
        'aj': "0"
    }

    headers = {"Accept-Encoding": "gzip, deflate",
               "Accept-Language": "zh-CN,zh;q=0.8",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4549.400 QQBrowser/9.7.12900.400",
               "Referer": "http://www.hashkill.com/",
               "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
               "Accept": "application/json, text/javascript, */*; q=0.01",
               "X-Requested-With": "XMLHttpRequest",
               "Connection": "keep-alive",
               "Host": "http://www.hashkill.com",
               "Origin": "http://www.hashkill.com",
               "Cookie":TransCookie(session.cookies.get_dict())
               }

    req_c = requests.Request("POST", HOST_C, data=data, headers=headers)
    resp_c = session.send(session.prepare_request(req_c), proxies=proxies)
    return resp_c.content


