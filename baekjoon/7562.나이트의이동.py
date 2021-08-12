import sys
# import time
# start = time.time()
sys.stdin = open('input.txt')
from collections import deque

t = int(input())
dx = [-2, -2, -1, 1, 2, 2, 1, -1]
dy = [-1, 1, 2, 2, 1, -1, -2, -2]

def bfs():
    q = deque()
    q.append((x1, y1))
    c = 0

    while q:
        x, y = q.popleft()
        if x == x2 and y == y2:
            return visit[x][y]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if visit[nx][ny] == 0:
                    visit[nx][ny] = visit[x][y] + 1
                    if nx == x2 and ny == y2:
                        return visit[nx][ny]

                    q.append((nx, ny))

for _ in range(t):
    n = int(input())
    visit = [[0]*n for _ in range(n)]
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    print(bfs())

# print(time.time()-start)