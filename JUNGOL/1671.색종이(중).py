import sys
sys.stdin = open('input.txt')
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    global ans
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 110 and 0 <= ny < 110:
            if arr[nx][ny] == 0:
                ans += 1


arr = [[0] * 110 for _ in range(110)]
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    for i in range(y, y + 10):
        for j in range(x, x + 10):
            arr[i][j] = 1

ans = 0
for i in range(110):
    for j in range(110):
        if arr[i][j] == 1:
            dfs(i, j)
print(ans)
