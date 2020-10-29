#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/5/25 10:16 
# @Author : 聂星星 
# @Version：V 0.1
# @File : get请求1.py
# @Desc :

from urllib.request import Request, urlopen

url = "https://www.baidu.com/s?wd=尚学堂"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}

request = Request(url, headers=headers)

urlopen(request)