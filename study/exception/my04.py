#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   my04.py
@Time    :   2020/04/29 10:34:40
@Author  :   Nie WeiXing 
@Version :   1.0
@Contact :   nwx_qdlg@163.com
@Desc    :   None
'''

# here put the import lib
import traceback

try:
    a = input("请输入一个被除数：")
    b = input("请输入一个除数：")
    c = float(a)/float(b)
except BaseException as e:
    with open("except.log","a") as f:
        traceback.print_exc(file=f)
else:
    print("计算结果是：",c)
finally:
    print("我是finally中的语句，无论发生异常与否，都执行")

print("程序结束")