

try:
    print("step01")
    a = 3/0
    print("step02")
except BaseException as e:
    print(e)
    print(type(e))

