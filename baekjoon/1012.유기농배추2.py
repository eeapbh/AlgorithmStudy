import sys
sys.setrecursionlimit(10**6)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0]*m for _ in range(n)]
    visit = [[0]*m for _ in range(n)]
    for i in range(k):
        a, b = map(int, input().split())
        arr[b][a] = 1
    cnt = 0
    def dfs(x, y):
        visit[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and arr[nx][ny] == 1 and visit[nx][ny] == 0:
                dfs(nx, ny)

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and visit[i][j] == 0:
                dfs(i, j)
                cnt += 1
    print(cnt)