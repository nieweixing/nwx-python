#循环输入数字，不是数字则异常处理，直到输入88结束

while True:
    try:
        x = int(input("请输入一个数字"))
        print(x)
        if x == 88:
            print("退出程序")
            break
    except BaseException as e:
        print(e)

print("循环数字输入程序结束")