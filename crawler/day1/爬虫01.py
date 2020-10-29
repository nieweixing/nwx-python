#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/5/25 9:35 
# @Author : 聂星星 
# @Version：V 0.1
# @File : 爬虫01.py
# @Desc : 第一个爬虫

from urllib.request import urlopen

url = "http://www.baidu.com"

response = urlopen(url)

info = response.read()

#打印内容
#print(info.decode())
print(response.getcode())
print(response.geturl())
print(response.info())