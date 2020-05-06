#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   study02.py
@Time    :   2020/05/06 10:11:25
@Author  :   Nie WeiXing 
@Version :   1.0
@Contact :   nwx_qdlg@163.com
@Desc    :   递归打开所有的目录和文件
'''

# here put the import lib

import os
import math

def getAllFiles(path):
    """
    递归文件夹目录
    """
    childFiles = os.listdir(path)
    for file in childFiles:
        filepath = os.path.join(path,file)
        print(filepath)
        if os.path.isdir(filepath):
            getAllFiles(filepath)