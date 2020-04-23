# -*- coding: utf-8 -*-

import psutil
import IPy
from subprocess import PIPE
from IPy import IP
import dns.resolver
import difflib
import filecmp
import smtplib
from functools import reduce

################################################################################

print(all([1,0,3,6]))

print(all([1,2,3]))

print(divmod(10,3))

################################################################################

# def ptf(a, b=5, c=10):
#   print(a+b+c)
 
# print(ptf(3, 7))
# print(ptf(25, c=24))
# print(ptf(c=50, a=100))
# print(ptf(c=50, a=100))

# def total(a=5, *numbers,):
#     for n in numbers:
#         a+=n
#     print(a)
# print(total(1,1,1,1,1))


# a = [0, 1, 2, 3, 4, 5, 6]
# print(a[1:3]) 
# print(a[2:] )
# print(a[:4] )
# print(a[:0])

# class A(object):
#     bar = 1
# a = A()
# print(getattr(a, 'bar'))

# a=list(range(10))
# print(a[::2])

# print(int("1001",2))


# a=[2,3,4,5]
# b=[2,5,8]

# print(list(set(a).intersection(set(b))))


# a=[1,2,3]
# new_a=[[a[2], a[0], a[1]], [a[1], a[2], a[0]], [a[0], a[1], a[2]]]

# print(new_a)


# lista=[[1,2,[3,4,[5,6]]],7,8,(9,10,(11,12))]
# a=reduce(lambda x,y:x+y,lista)
# print(a)

################################################################################

# text1 = """text1 is fdasgfdsgfdsgdfgdsfgsdgfdg
# hgfhfgdhdgfghdghgfdh text1 gfdsgfdsgdfsgfd
# """
# text1_content = text1.splitlines()

# text2 = """text2 is fdasgfdsgfdsgdfgdsfgsdgfdg
# hgfhfgdhdgfghdghgfdh text2 gfdsgfdsgdfsgfd
# """
# text2_content = text2.splitlines()

# d = difflib.Differ()
# diff = d.compare(text1_content, text2_content)
# print('\n'.join(list(diff)))

# d = difflib.HtmlDiff()
# d_html = d.make_file(text1_content, text2_content)
# print(d_html)

################################################################################


#domain = input('please input an domain:')
# a = dns.resolver.query("www.baidu.com")
# for i in a.response.answer:
#   for j in i.items:
#     print(j.address())


#print(psutil.cpu_times())
#print(psutil.cpu_count(logical=False))
#print(psutil.virtual_memory())


# mem = psutil.virtual_memory()

# print(mem.total)
# print(mem.free)


# print(psutil.disk_usage)

# print(psutil.users)

# print(psutil.pids())

# p = psutil.Process(28392)
# print(p.name())
# print(p.exe())


# p = psutil.Popen(["C:\\Users\\12207\\Python\\Python37\\python.exe", "print('hello')"], stdout=PIPE)
# print(p.name)
################################################################################

# v = IP('192.168.30.30/32').version()
# print(v)
# v1 = IP('::1').version()
# print(v1)

# ip = IP('10.0.3.0/28')
# print(ip.len())
# for i in ip:
#   print(i) 

# ip1 = IP('161.189.48.95').reverseNames()
# print(ip1)