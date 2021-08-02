import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
visit = []
def bfs():
    q = deque()
    q.append((0, 0, 1))
    cnt = 0
    while q:
        cx, cy, cc = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            nc = cc + 1
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visit:
                if arr[nx][ny] == 1:
                    q.append((nx, ny, nc))
                    visit.append((nx, ny, nc))
                if nx == n-1 and ny == m-1:
                    return nc

print(bfs())





