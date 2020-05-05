import csv

with open(r"C:\Users\nieweixing\Desktop\python\study\file\test.txt","r",encoding="utf-8") as f:
    # a = f.readlines()
    # print(type(a))
    for i in f:
        print(i,end="")
