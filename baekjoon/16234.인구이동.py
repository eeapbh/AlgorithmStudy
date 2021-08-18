from collections import deque
import sys
n, l, r = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    save = []
    save.append((x, y))
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if visit[nx][ny] == 0 and l<=abs(arr[cx][cy] - arr[nx][ny])<=r:
                    visit[nx][ny] = 1
                    save.append((nx, ny))
                    q.append((nx, ny))
    return save


cnt = 0
while 1:
    trg = 0
    visit = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                visit[i][j] = 1
                save = bfs(i, j)
                if len(save) > 1:
                    trg = 1
                    num = sum(arr[x][y] for x, y in save)//len(save)
                    for x, y in save:
                        arr[x][y] = num
    if trg == 0:
        break
    cnt += 1

print(cnt)


