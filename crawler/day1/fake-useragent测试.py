#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/5/25 10:11 
# @Author : 聂星星 
# @Version：V 0.1
# @File : fake-useragent测试.py
# @Desc :

from fake_useragent import UserAgent

ua = UserAgent()
print(ua.chrome)
print(ua.firefox)