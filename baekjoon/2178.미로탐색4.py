import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
n, m = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
arr = [list(map(int, input())) for _ in range(n)]
def bfs():
    q = deque()
    q.append((0, 0, 0))
    visit = [(0, 0)]
    while q:
        cx, cy, cc = q.popleft()
        if cx == n-1 and cy == m-1:
            print(cc+1)
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if arr[nx][ny] == 1 and (nx, ny) not in visit:
                    q.append((nx, ny, cc + 1))
                    visit.append((nx, ny))


bfs()
