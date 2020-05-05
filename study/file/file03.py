#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   file03.py
@Time    :   2020/04/30 10:47:07
@Author  :   Nie WeiXing 
@Version :   1.0
@Contact :   nwx_qdlg@163.com
@Desc    :   图片拷贝
'''

# here put the import lib

with open(r"C:\Users\nieweixing\Desktop\test.jpg","rb") as f:
    with open("aa.jpg","wb") as w:
        for line in f.readlines():
            w.write(line)

print("图片拷贝成功")
