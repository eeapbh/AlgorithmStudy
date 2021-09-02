import sys
sys.setrecursionlimit(1000000)
n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dp = [[0]*n for _ in range(n)]


def dfs(x, y):
    if dp[x][y]:
        return dp[x][y]
    dp[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if arr[nx][ny] > arr[x][y]:
                dp[x][y] = max(dp[x][y], dfs(nx, ny)+1)
    return dp[x][y]


ans = 1
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i, j))
print(ans)
