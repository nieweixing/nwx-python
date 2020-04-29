arr1 = input("请输入第一个数组：")
a = [int(n) for n in arr1.split()] 
arr2 = input("请输入第一个数组：")
b = [int(n) for n in arr2.split()] 

new_dicts = {}
value_lists = []
# new_list = []
result = []
k = 5

for i in a:
    for j in b:
        print(i, j) 
        sum = i+j
        print(i+j)
        new_dicts[sum] = "[{0}, {1}]".format(i, j)
print(new_dicts)
 
new_list = sorted([x for x in new_dicts.keys()])
# for i in new_dicts.keys():
#     value_lists.append(i)
# #print(value_lists)
# else:
# new_list = sorted(value_lists)
# print(new_list)

for i in range(0,k):
    result.append(new_dicts[new_list[i]])
print(result)

for i in result:
    print(i,end="\t")