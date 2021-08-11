import sys
from collections import deque
m, n, h = map(int, sys.stdin.readline().split())
arr = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]
#상 하 좌 우 위 아래
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
q = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] ==1:
                q.append((j, k, i, 0))


def bfs():
    c = 0
    while q:
        x, y, z, c = q.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0<=nx<n and 0<=ny<m and 0<=nz<h and arr[nz][nx][ny] == 0:
                arr[nz][nx][ny] = 1
                q.append((nx, ny, nz, c + 1))
    return c
ans = bfs()

def check(ans):
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if arr[i][j][k] == 0:
                    return -1

    return ans
print(check(ans))
