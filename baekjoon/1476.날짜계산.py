a, b, c = map(int, input().split())
n = 1
def fa(x):
    if x % 15 == 0:
        return 15
    else:
        return x % 15

def fb(x):
    if x % 28 == 0:
        return 28
    else:
        return x % 28

def fc(x):
    if x % 19 == 0:
        return 19
    else:
        return x % 19


while 1:
    if fa(n) == a and fb(n) == b and fc(n) == c:
        print(n)
        break
    n += 1
