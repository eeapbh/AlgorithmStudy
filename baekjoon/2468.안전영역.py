import sys
sys.setrecursionlimit(100000)
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
m = 0
M = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y, h):
    visit[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and visit[nx][ny] == 0 and arr[nx][ny]>h:
            dfs(nx, ny, h)


for i in range(n):
    for j in range(n):
        if arr[i][j] > M:
            M = arr[i][j]

ans = -1
for h in range(m, M + 1):
    cnt = 0
    visit = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j]>h and visit[i][j] == 0:
                dfs(i, j, h)
                cnt += 1

    if ans < cnt:
        ans = cnt
print(ans)