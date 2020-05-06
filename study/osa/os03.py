#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   os03.py
@Time    :   2020/05/06 09:29:48
@Author  :   Nie WeiXing 
@Version :   1.0
@Contact :   nwx_qdlg@163.com
@Desc    :   walk方法遍历目录
'''

# here put the import lib

import os

path = os.getcwd()

dir_list = os.walk(path)

for dirpath, dirnames, filenames in dir_list:
    print(dirpath)