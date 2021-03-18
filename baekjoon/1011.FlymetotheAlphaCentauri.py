import math
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    d = b - a
    if d < 4:
        print(d)
    else:
        num = int(math.sqrt(d))
        if d == num * 2:
            print(num*2 - 1)
        elif d <= num ** 2 + num:
            print(num * 2)
        elif d > num ** 2 + num:
            print(num * 2 + 1)



