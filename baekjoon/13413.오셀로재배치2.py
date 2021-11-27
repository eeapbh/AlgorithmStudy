t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    b = input()
    cnt = 0
    for i in range(n):
        if a[i] != b[i]:
            cnt += 1
    d1 = a.count('W')
    d2 = b.count('W')
    print(abs(d1-d2) + (cnt -abs(d1-d2))//2)

