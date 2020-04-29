#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   my06.oy
@Time    :   2020/04/29 14:36:25
@Author  :   Nie WeiXing 
@Version :   1.0
@Contact :   nwx_qdlg@163.com
@Desc    :   自定义异常类
'''

# here put the import lib

class AgeError(Exception):
    def __init__(self, errorInfo):
        Exception.__init__(self)
        self.errorInfo = errorInfo
    
    def __str__(self):
        return str(self.errorInfo) + "年龄错误"


if __name__ == "__main__":
    age = int(input("请输出一个年龄"))
    if age<1 or age>150:
        raise AgeError(age)
    else:
        print("正常的年龄",age)