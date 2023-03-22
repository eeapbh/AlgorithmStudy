from collections import deque
n, k = map(int, input().split())

memo = [0]*100001

def bfs(n, k):
    q = deque()
    q.append((n, 0))
    cnt = 0
    rs = []
    while q:
        x, c = q.popleft()
        if x == k:

            rs.append(c)
        memo[x] = 1
        for i in (x-1, x+1, 2*x):
            if 0 <= i <= 100000:
                if memo[i] == 0:
                    q.append((i, c+1))
    return min(rs), rs.count(min(rs))

a, b = bfs(n, k)
print(a)
print(b)

