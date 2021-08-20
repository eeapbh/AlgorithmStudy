from collections import deque
import sys
n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visit[x][y] = 1
    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if arr[nx][ny] == 0:
                    water[cx][cy] += 1
                if arr[nx][ny] != 0 and visit[nx][ny] == 0:
                    q.append((nx, ny))
                    visit[nx][ny] = 1

ans = 0
while 1:

    cnt = 0
    visit = [[0] * m for _ in range(n)]
    water = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0 and visit[i][j] == 0:
                bfs(i, j)
                cnt += 1
    # print(water)
    for i in range(n):
        for j in range(m):
            arr[i][j] -= water[i][j]
            if arr[i][j] < 0:
                arr[i][j] = 0
    if cnt >= 2:
        print(ans)
        break
    if cnt == 0:
        print(0)
        break
    ans += 1