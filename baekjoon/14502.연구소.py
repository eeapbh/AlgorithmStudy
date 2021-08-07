import sys
n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
from itertools import combinations
from copy import deepcopy
save = []
virus = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visit = [[0]*m for _ in range(n)]
def dfs(x, y):
    arr2[x][y] = 2
    visit[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx < n and 0<=ny < m and arr2[nx][ny] != 1 and visit[nx][ny] == 0:
            dfs(nx, ny)



for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            save.append((i, j))
        if arr[i][j] == 2:
            virus.append((i, j))


comb = list(combinations(save, 3))
# print(comb)
# print(virus)
cnt = 0
M = 0
for c in comb:
    arr2 = deepcopy(arr)

    for i in c:
        arr2[i[0]][i[1]] = 1
    visit = [[0] * m for _ in range(n)]
    for v in virus:
        dfs(v[0], v[1])
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr2[i][j] == 0:
                cnt += 1
    # print(cnt)
    if cnt > M:
        M = cnt
print(M)