
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   my03.py
@Time    :   2020/04/29 10:09:56
@Author  :   Nie WeiXing 
@Version :   1.0
@Contact :   nwx_qdlg@163.com
@Desc    :   测试多个exception结构
'''

# here put the import lib

try:
    a = input("请输入一个被除数：")
    b = input("请输入一个除数：")
    c = float(a)/float(b)
    print(c)
except ZeroDivisionError:
    print("异常,不能除以0")
except ValueError:
    print("异常，不能讲字符串转化为数字")
except NameError:
    print("异常，变量不存在")
except BaseException as e:
    print(e)
else:
    print("计算结果是：",c)