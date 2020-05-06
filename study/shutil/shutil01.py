#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   shutil01.py
@Time    :   2020/05/06 09:41:59
@Author  :   Nie WeiXing 
@Version :   1.0
@Contact :   nwx_qdlg@163.com
@Desc    :   None
'''

# here put the import lib

import shutil
import zipfile

#shutil.copy("aa.jpg","aa1.jpg")

#shutil.copytree("hello/","test",ignore=shutil.ignore_patterns("*.txt"))

#shutil.make_archive("test/b/test","tar.gz","hello/b/")

#f = zipfile.ZipFile("aa.tar.gz","w")
#f.write("aa.jpg")

f = zipfile.ZipFile("../../aa.tar.gz","r")
f.extractall("../../")
f.close()