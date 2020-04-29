#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   my05.py
@Time    :   2020/04/29 11:16:38
@Author  :   Nie WeiXing 
@Version :   1.0
@Contact :   nwx_qdlg@163.com
@Desc    :   with上下文管理
'''

# here put the import lib
with open(r"C:\Users\nieweixing\Desktop\python\study\exception\test.txt", "r") as f:
    content = f.readline()
    print(content)