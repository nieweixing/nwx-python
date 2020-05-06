a = 100

def test(n):
    print("n:",id(n))
    n = n+200
    print("n:",id(n))
    print(n)

test(a)
print(a)