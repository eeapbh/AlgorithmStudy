import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
n, m = map(int, input().split())
arr = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    s, e = map(int, input().split())
    arr[s][e] = 1

visit = [0]*(n+1)
def bfs(x):
    q.append(x)
    while q:
        cx = q.popleft()
        visit[cx] = 1
        for i in range(n+1):
            if arr[cx][i] == 1 and visit[i] == 0:
                q.append(i)
                arr[cx][i] = 0


ans = 0
q = deque()
for i in range(1, n+1):
    if visit[i] == 0:
        bfs(i)
        ans += 1

print(ans)