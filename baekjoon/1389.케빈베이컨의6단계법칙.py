import sys

from collections import deque
n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
visit = [[-1]*(n+1) for _ in range(n+1)]
def bfs(s):
    q = deque()
    q.append((s, 0))
    visit[s][s] = 0
    while q:
        x, c = q.popleft()
        for i in arr[x]:
            if visit[s][i] == -1:
                visit[s][i] = c + 1
                q.append((i, c+1))


for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(1, n+1):
    bfs(i)
ans = []
for a in range(1, n+1):
    ans.append(sum(visit[a]))
print(ans.index(min(ans)) + 1)