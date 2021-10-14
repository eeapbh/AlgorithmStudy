n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visit = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    global cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and arr[nx][ny] == 1:
            if (nx, ny) not in visit:
                cnt += 1
                visit.append((nx, ny))
                dfs(nx, ny)

rs = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and (i, j) not in visit:
            cnt = 1
            visit.append((i, j))
            dfs(i, j)
            rs.append(cnt)

print(len(rs))
rs.sort()
print(*rs)