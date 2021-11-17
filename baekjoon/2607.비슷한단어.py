n = int(input())
word = list(input())
ans = 0
for _ in range(n-1):
    a = word[:]
    b = list(input())
    for i in range(len(b)):
        p = b.pop(0)
        if p in a:
            a.remove(p)
        else:
            b.append(p)
    A = len(a)
    B = len(b)
    if A == 0 and B == 0 or A == 1 and B == 0 or A == 0 and B == 1 or A == 1 and B == 1:
        ans += 1
print(ans)