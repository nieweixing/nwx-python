#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/5/25 9:46 
# @Author : 聂星星 
# @Version：V 0.1
# @File : Request的使用.py
# @Desc :

from urllib.request import urlopen
from urllib.request import Request
from random import choice

url = "http://www.baidu.com"

user_agents=[
    "User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0",
    "User-Agent:Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
]

headers = {
    "User-Agent": choice(user_agents)

}

request = Request(url,headers=headers)

#print(request.get_header('User-agent'))

response = urlopen(request)


info = response.read()

print(info.decode())