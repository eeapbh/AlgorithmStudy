from collections import deque
import sys
m, n, k = map(int, sys.stdin.readline().split())
arr = [[0]*n for _ in range(m)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visit = [[0]*n for _ in range(m)]
ans = []
def bfs(x, y):
    q = deque()
    q.append((x, y))
    w = 0
    while q:
        w += 1
        x, y = q.popleft()
        visit[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n and arr[nx][ny] == 0 and visit[nx][ny] == 0:
                if (nx, ny) not in q:
                    q.append((nx, ny))
    ans.append(w)
for i in range(k):
    s1, s2, e1, e2 = map(int, sys.stdin.readline().split())
    for i in range(s2, e2):
        for j in range(s1, e1):
            arr[i][j] = 1

cnt = 0

for i in range(m):
    for j in range(n):
        if arr[i][j] == 0 and visit[i][j] == 0:
            bfs(i, j)
            cnt += 1
ans.sort()
print(cnt)
print(*ans)