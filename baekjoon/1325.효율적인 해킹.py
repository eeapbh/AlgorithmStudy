import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def bfs(x):
    q = deque()
    q.append(x)
    cnt = 0
    visit = [0]*(n+1)
    visit[x] = 1
    while q:
        cx = q.popleft()
        for i in arr[cx]:
            if visit[i] == 0:
                visit[i] = 1
                q.append(i)
                cnt += 1
    return cnt
n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    arr[b].append(a)

ans = 0
rs = []
for i in range(1, n + 1):
    tmp = bfs(i)
    if ans == tmp:
        rs.append(i)
    if ans < tmp:
        ans = tmp
        rs = []
        rs.append(i)

print(*rs)
