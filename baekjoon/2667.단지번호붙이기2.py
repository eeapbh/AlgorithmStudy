import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
arr = [list(input()) for _ in range(n)]
visit = [[0]*n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
save = []

def dfs(x, y):
    global cnt
    cnt += 1
    visit[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0<=ny < n and visit[nx][ny] == 0 and arr[nx][ny] == '1':

            dfs(nx, ny)
    return cnt


for i in range(n):
    for j in range(n):
        if arr[i][j] == '1' and visit[i][j] == 0:
            cnt = 0
            dfs(i, j)
            # if cnt == 0:
            #     cnt += 1
            save.append(cnt)
save.sort()
print(len(save))
for i in save:
    print(i)