# -*- coding: UTF-8 -*-
 
import turtle 

#turtle.circle(50)

s = (x*2 for x in range(5))

print(s.__next__())
print(s.__next__())
print(s.__next__())


#num = input("请输出一个数字：")
#print(num if int(num) > 10 else "数字小于10")

print("#####################################")

sum_all = 0
sum_odd = 0
sum_even = 0
for x in range(101):
    sum_all += x
    if x%2 == 1:
        sum_odd += x
    else:
        sum_even += x
print("1-100累计的总和{0},奇数和为{1}，偶数和为{2}".format(sum_all,sum_odd,sum_even))

print("#####################################")

for x in range(5):
    for y in range(5):
        print(x, end="\t")
    print()

print("#####################################")

for m in range(1, 10):
    for n in range(1, m+1):
        print("{0}*{1}={2}".format(m,n,(m*n)),end = "\t")
    print()