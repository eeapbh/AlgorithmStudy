import sys
n, k = map(int, sys.stdin.readline().split())

visit = set()
for _ in range(k):
    a = int(sys.stdin.readline())
    ans = 0
    tmp = a
    while tmp > 1:
        if tmp in visit:
            ans = tmp
        tmp //= 2
    visit.add(a)
    print(ans)
