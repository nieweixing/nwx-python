#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   study_py01.py
@Time    :   2020/05/06 10:00:19
@Author  :   Nie WeiXing 
@Version :   1.0
@Contact :   nwx_qdlg@163.com
@Desc    :   递归算法
'''

# here put the import lib

# num = 1
# def a1():
#     global num  #在函数中改变全局变量的值，需要用global关键字
#     num +=1
#     print("a1")
#     if num < 10:
#         a1()

# def b1():
#     print("b1")

# a1()


def factorial(n):
    if n == 1:
        return n
    else: 
        return n*factorial(n-1)

print(factorial(5))