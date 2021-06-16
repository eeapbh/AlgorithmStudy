import sys
sys.stdin = open('input.txt','r')


n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
tmp1 = []
tmp2 = []
for a in arr:
    if a <= 0:
        tmp1.append(a)
    else:
        tmp2.append(a)
ans = 0

if 0 in tmp1:
    if len(tmp1) % 2 == 0:
        a = tmp1.pop()
        b = tmp1.pop()
        ans += a * b
        while len(tmp1):
            a = tmp1.pop(0)
            b = tmp1.pop(0)
            ans += a * b
    else:
        tmp1.pop()
        while len(tmp1):
            a = tmp1.pop(0)
            b = tmp1.pop(0)
            ans += a * b
else:
    while 1:
        if len(tmp1) == 0:
            break
        if len(tmp1) == 1:
            ans += tmp1.pop(0)
            break
        a = tmp1.pop(0)
        b = tmp1.pop(0)
        ans += a * b

while 1:
    if len(tmp2) == 0:
        break
    if len(tmp2) == 1:
        ans += tmp2.pop()
        break
    a = tmp2.pop()
    b = tmp2.pop()
    if 1 in (a, b):
        ans += a + b
    else:
        ans += a * b

print(ans)





