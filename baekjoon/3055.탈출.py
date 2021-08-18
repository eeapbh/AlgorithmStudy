# import sys
# sys.stdin = open('input.txt', 'r')

from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
visitw = [[0]*m for _ in range(n)]
visits = [[0]*m for _ in range(n)]
water = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'D':
            bx, by = i, j
        if arr[i][j] == 'S':
            gx, gy = i, j
        if arr[i][j] == '*':
            water.append((i, j, 0))

def bfs():
    q = deque()
    for w in water:
        q.append(w)

    q.append((gx, gy, 0))
    while q:
        x, y, c = q.popleft()
        if arr[x][y] == '*':
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<n and 0<=ny<m:
                    if visitw[nx][ny] == 0 and arr[nx][ny] == '.':
                        arr[nx][ny] = '*'
                        visitw[nx][ny] = 1
                        q.append((nx, ny, c+1))
        if arr[x][y] == 'S':
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if arr[nx][ny] == 'D':
                        return c + 1
                    if visits[nx][ny] == 0 and arr[nx][ny] != '*' and arr[nx][ny] != 'X':
                        visits[nx][ny] = 1
                        arr[x][y] = '.'
                        arr[nx][ny] = 'S'
                        q.append((nx, ny, c + 1))
    return 'KAKTUS'
print(bfs())





