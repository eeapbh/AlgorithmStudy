import sys

from collections import deque
sys.setrecursionlimit(10000000)
def dfs(x, y):
    visit1.append((x, y))
    arr[x][y] = flag
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visit1:
            if arr[nx][ny] != 0:
                dfs(nx, ny)


def bfs(num):
    global ans
    dist = [[-1]*n for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(n):
            if arr[i][j] == num:
                q.append((i, j))
                dist[i][j] = 0
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if arr[nx][ny] != num and arr[nx][ny]> 0:
                    ans = min(ans, dist[cx][cy])
                    return
                elif arr[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[cx][cy] + 1
                    q.append((nx, ny))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visit1 = []
flag = 1
for i in range(n):
    for j in range(n):
        if (i, j) not in visit1 and arr[i][j] != 0:
            dfs(i, j)
            flag += 1

ans = 987654321
for i in range(1, flag):
    bfs(i)
print(ans)


