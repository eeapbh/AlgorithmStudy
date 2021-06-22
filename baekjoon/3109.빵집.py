import sys
sys.stdin = open('input.txt', 'r')
r, c = map(int, input().split())
dx = [-1, 0, 1]
dy = [1, 1, 1]

arr = [list(input()) for _ in range(r)]
visit = [[0]*c for _ in range(r)]

cnt = 0
def dfs(x, y):
    global cnt
    if y == c-1:
        cnt += 1
        return

    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] == '.':
            if visit[nx][ny] == 0:
                visit[nx][ny] = 1
                return dfs(nx, ny)

for i in range(r):
    dfs(i, 0)
print(cnt)