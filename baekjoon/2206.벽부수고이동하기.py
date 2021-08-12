import sys
from collections import deque
# sys.setrecursionlimit(1000000)
# sys.stdin = open('input.txt', 'r')
n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visit = [[[0]*2 for _ in range(m)] for _ in range(n)]

def bfs():
    q = deque()
    q.append([0, 0, 0])
    visit[0][0][0] = 1
    while q:
        x, y, w = q.popleft()
        if x == n-1 and y == m-1:
            return visit[x][y][w]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if arr[nx][ny] == 1 and w == 0:
                    visit[nx][ny][1] = visit[x][y][0] + 1
                    q.append((nx, ny, 1))
                elif arr[nx][ny] == 0 and visit[nx][ny][w] == 0:
                    visit[nx][ny][w] = visit[x][y][w] + 1
                    q.append((nx, ny, w))
bfs()

ans1, ans2 = visit[n-1][m-1][0], visit[n-1][m-1][1]
# print(ans1, ans2)
if ans1 == 0 and ans2 != 0:
    print(ans2)
elif ans1 != 0 and ans2 == 0:
    print(ans1)
elif ans1 == 0 and ans2 == 0:
    print(-1)
else:
    print(min(ans1, ans2))

