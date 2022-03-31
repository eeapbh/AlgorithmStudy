a, b = map(int, input().split())

l = 0
r = 0

while 1:
    if a == 1 and b == 1:
        break
    if a < b:
        r += 1
        b -= a
    else:
        l += 1
        a -= b

print(l, r)


