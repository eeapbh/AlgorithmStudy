import sys

r, c = map(int, sys.stdin.readline().split())
arr = [list(map(lambda x:ord(x)-65, sys.stdin.readline())) for _ in range(r)]
visit = [0]*26
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 1
visit[arr[0][0]] = 1
def dfs(x, y, v):
    global ans
    ans = max(v, ans)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<r and 0<=ny<c and visit[arr[nx][ny]] == 0:
            visit[arr[nx][ny]] = 1
            dfs(nx, ny, v + 1)
            visit[arr[nx][ny]] = 0

dfs(0, 0, ans)
print(ans)