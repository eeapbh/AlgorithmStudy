from collections import deque
m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
q = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i, j, 0))
def bfs():
    cc = 0
    while q:
        cx, cy, cc = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx < n and 0<=ny < m and arr[nx][ny] == 0:
                q.append((nx, ny, cc + 1))
                arr[nx][ny] = 1
    return cc
ans = bfs()
check = 0
for i in range(n):
    check += arr[i].count(0)
if check == 0:
    print(ans)
else:
    print(-1)