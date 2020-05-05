#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   os02.py
@Time    :   2020/05/04 19:54:07
@Author  :   Nie WeiXing 
@Version :   1.0
@Contact :   nwx_qdlg@163.com
@Desc    :   测试os模块，文件和目录的操作
'''

# here put the import lib
import os.path

print(os.name)
print(os.sep)
print(repr(os.linesep))
print(os.stat(r"C:\Users\nieweixing\Desktop\python\study\os\os02.py"))
print(os.getcwd())
#os.chdir(r"C:\Users\nieweixing\Desktop\python\study\os")
#os.mkdir("os-test")
#os.rmdir("os-test")
#os.removedirs("a/b/v/b")
#os.makedirs("a/b/c")

#os.rename("a","hello")

dirs = os.listdir(r"C:\Users\nieweixing\Desktop\python")
print(dirs)